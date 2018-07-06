import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/** note: submenu only apppear when children.length>=1
 *   detail see  https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 **/

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']     will control the page roles (you can set multiple roles)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if true ,the page will no be cached(default is false)
  }
 **/
export const constantRouterMap = [
  { path: '/login', component: () => import('../views/login/index'), hidden: true },
  { path: '/error', component: () => import('../views/error/error'), hidden: true },
  {
    path: '/',
    component: Layout,
    redirect: 'index/userIndex',
    children: [{
      path: 'index/userIndex',
      component: () => import('../views/index/userIndex'),
      name: 'userIndex',
      meta: { title: 'userIndex', icon: 'userIndex', noCache: true }
    },{
      path: 'index/adminIndex',
      component: () => import('../views/index/adminIndex'),
      name: 'adminIndex',
      meta: { title: 'adminIndex', icon: 'adminIndex', noCache: true }
    }
    ],

  },
  {
    path: '/jurisdiction',
    component: Layout,
    redirect: 'jurisdiction/admin',
    children: [{
      path: 'admin',
      component: () => import('../views/jurisdiction/admin'),
      name: 'admin',
      meta: { title: 'admin', icon: 'admin', noCache: true }
    },{
      path: 'user',
      component: () => import('../views/jurisdiction/user'),
      name: 'user',
      meta: { title: 'user', icon: 'user', noCache: true }
    }
    ],

  },
  {
    path: '/commodity',
    component: Layout,
    redirect: 'commodity/commodityManagement',
    children: [{
      path: 'commodityManagement',
      component: () => import('../views/commodity/commodityManagement'),
      name: 'commodityManagement',
      meta: {title: 'commodityManagement', icon: 'commodityManagement', noCache: true}
    }, {
      path: 'commodityGroup',
      component: () => import('../views/commodity/commodityGroup'),
      name: 'commodityGroup',
      meta: {title: 'commodityGroup', icon: 'commodityGroup', noCache: true}
    }, {
      path: 'goodsImported',
      component: () => import('../views/commodity/goodsImported'),
      name: 'goodsImported',
      meta: {title: 'goodsImported', icon: 'goodsImported', noCache: true}
    }
    ]
  },{
    path: '/order',
    component: Layout,
    redirect: 'order/commodityManagement',
    children: [{
      path: 'allOrder',
      component: () => import('../views/order/allOrder'),
      name: 'allOrder',
      meta: {title: 'allOrder', icon: 'allOrder', noCache: true}
    }, {
      path: 'orderIndex',
      component: () => import('../views/order/orderIndex'),
      name: 'orderIndex',
      meta: {title: 'orderIndex', icon: 'orderIndex', noCache: true}
    }, {
      path: 'refund',
      component: () => import('../views/order/refund'),
      name: 'refund',
      meta: {title: 'refund', icon: 'refund', noCache: true}
    }
    ]
  },{
    path: '/activity',
    component: Layout,
    redirect: 'activity/discountCoupon',
    children: [{
      path: 'discountCoupon',
      component: () => import('../views/activity/discountCoupon'),
      name: 'discountCoupon',
      meta: {title: 'discountCoupon', icon: 'discountCoupon', noCache: true}
    }, {
      path: 'storeActivity',
      component: () => import('../views/activity/storeActivity'),
      name: 'storeActivity',
      meta: {title: 'storeActivity', icon: 'storeActivity', noCache: true}
    }
    ]
  }


]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

