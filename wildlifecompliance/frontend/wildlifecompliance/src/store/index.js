import 'es6-promise/auto'
import Vue from 'vue'
import Vuex from 'vuex'
import { applicationStore } from './modules/application'
import { userStore } from './modules/user'
import { rendererStore } from './modules/renderer'
import { callemailStore } from './modules/call_email'
import { complianceRendererStore } from './modules/compliance_renderer'

Vue.use(Vuex);

export default new Vuex.Store({
	state: {},
	mutations: {},
	getters: {},
	modules: {
		appStore: applicationStore,
		userStore: userStore,
		rendererStore: rendererStore,
		callemailStore: callemailStore,
		complianceRendererStore: complianceRendererStore,
	},
	createHelpers: function(names) {
		const res = {}
		names.forEach(name => {
		  res[name] = createNamespacedHelpers(name)
		})
		return res
	  },
})
