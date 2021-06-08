from setuptools import setup

setup(name='ledger',
      version='2.0',
      description='Ledger Payments App',
      url='https://github.com/dbca-wa/ledger',
      author='Department of Parks and Wildlife',
      author_email='asi@dbca.wa.gov.au',
      license='BSD',
      packages=['ledger','ledger.accounts','ledger.api','ledger.accounts.management','ledger.accounts.management.commands','ledger.accounts.migrations','ledger.accounts.templates',
                'ledger.address','ledger.address.fixtures','ledger.address.migrations',
                'ledger.basket','ledger.basket.migrations',
                'ledger.catalogue','ledger.catalogue.migrations',
                'ledger.checkout',
                'ledger.dashboard','ledger.dashboard.catalogue',
                'ledger.emails',
                'ledger.licence','ledger.licence.migrations',
                'ledger.order','ledger.order.migrations',
                'ledger.partner',
                'ledger.payment','ledger.payment.migrations',
                'ledger.payments','ledger.payments.bpay','ledger.payments.bpoint','ledger.payments.cash','ledger.payments.invoice','ledger.payments.management','ledger.payments.migrations','ledger.payments.static.payments','ledger.payments.templates.dpaw_payments','ledger.payments.templatetags',
                'ledger.payments.bpay.dashboard','ledger.payments.bpay.management','ledger.payments.bpay.management.commands','ledger.payments.bpay.migrations',
                'ledger.payments.bpoint.BPOINT','ledger.payments.bpoint.dashboard','ledger.payments.bpoint.management','ledger.payments.bpoint.management.commands','ledger.payments.bpoint.migrations',
                'ledger.payments.cash.fixtures','ledger.payments.cash.migrations',
                'ledger.payments.invoice.dashboard','ledger.payments.invoice.migrations',
                'ledger.payments.static.payments.img','ledger.payments.static.payments.js',
                'ledger.static.ledger','ledger.static.ledger.css','ledger.static.ledger.fonts','ledger.static.ledger.images',
                'ledger.taxonomy',
                'ledger.templates','ledger.templates.basket.partials','ledger.templates.checkout','ledger.templates.email','ledger.templates.partials',
                ],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
