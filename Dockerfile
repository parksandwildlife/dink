# Prepare the base environment.
FROM ubuntu:22.04 as builder_base_ledgergw
MAINTAINER asi@dbca.wa.gov.au
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Australia/Perth
ENV PRODUCTION_EMAIL=True
ENV SECRET_KEY="ThisisNotRealKey"

# Use Australian Mirrors
RUN sed 's/archive.ubuntu.com/au.archive.ubuntu.com/g' /etc/apt/sources.list > /etc/apt/sourcesau.list
RUN mv /etc/apt/sourcesau.list /etc/apt/sources.list
# Use Australian Mirrors

RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install --no-install-recommends -y wget git libmagic-dev gcc binutils libproj-dev gdal-bin python3 python3-setuptools python3-dev python3-pip tzdata cron
RUN apt-get install --no-install-recommends -y libpq-dev patch build-essential software-properties-common ca-certificates bzip2 gpg-agent
RUN update-ca-certificates
RUN apt-get install --no-install-recommends -y postgresql-client mtr htop vim ssh


RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install --no-install-recommends -y python3.7 python3.7-dev python3.7-distutils
RUN ln -s /usr/bin/python3.7 /usr/bin/python && python3.7 -m pip install --upgrade pip==21.3.1
RUN apt-get update

#RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
# Install Python libs from requirements.txt.
FROM builder_base_ledgergw as python_libs_ledgergw
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt \
  # Update the Django <1.11 bug in django/contrib/gis/geos/libgeos.py
  # Reference: https://stackoverflow.com/questions/18643998/geodjango-geosexception-error
  #&& sed -i -e "s/ver = geos_version().decode()/ver = geos_version().decode().split(' ')[0]/" /usr/local/lib/python3.6/dist-packages/django/contrib/gis/geos/libgeos.py \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

COPY libgeos.py.patch /app/
RUN patch /usr/local/lib/python3.7/dist-packages/django/contrib/gis/geos/libgeos.py /app/libgeos.py.patch
RUN rm /app/libgeos.py.patch

# Install the project (ensure that frontend projects have been built prior to this step).
FROM python_libs_ledgergw
COPY timezone /etc/timezone
ENV TZ=Australia/Perth
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY gunicorn.ini manage_ledgergw.py ./
COPY ledger ./ledger
COPY bin ./bin
RUN touch /app/.env
COPY ledgergw ./ledgergw
COPY cron /etc/cron.d/ledgergw
COPY startup.sh /
RUN python manage_ledgergw.py collectstatic --noinput
# RUN service rsyslog start
RUN chmod 0644 /etc/cron.d/ledgergw
RUN crontab /etc/cron.d/ledgergw
RUN service cron start
RUN touch /var/log/cron.log
RUN service cron start
RUN chmod 755 /app/bin/*
RUN chmod 755 /startup.sh

# kubernetes health checks script
RUN wget https://raw.githubusercontent.com/dbca-wa/wagov_utils/main/wagov_utils/bin/health_check.sh -O /bin/health_check.sh
RUN chmod 755 /bin/health_check.sh

EXPOSE 8080
HEALTHCHECK --interval=1m --timeout=5s --start-period=10s --retries=3 CMD ["wget", "-q", "-O", "-", "http://localhost:8080/"]
CMD ["/startup.sh"]
#CMD ["gunicorn", "ledgergw.wsgi", "--bind", ":8080", "--config", "gunicorn.ini"]
