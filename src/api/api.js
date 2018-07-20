// const title = 'http://10.0.0.197:7443/sharp/manager/';
const title = 'http://120.79.182.43:7443/sharp/manager/';

const api={
  login: title + 'user/login',//用户登录
  changePwd: title + 'user/update_user',//修改密码

  get_all_order: title + 'order/order_list',//获取所有订单

  get_all_product: title + 'product/get_all',//获取所有商品
  update_product: title + 'product/update_product',//上架/下架商品
  get_first_category: title + 'category/get_first',//获取类目
  get_child_category:title + 'category/get_child',//获取子类目
  get_categorybrands: title + 'category/get_categorybrands',//根据类目id获取商品属性
  get_category_by_prname: title + 'category/get_category_by_prname',//搜索商品对应的类目
  get_ctlist_by_ctid: title + 'category/get_ctlist_by_ctid',//根据最后一层CTid获取对应的类目
}

export default api
