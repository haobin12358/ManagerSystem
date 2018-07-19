const title = 'http://10.0.0.197:7443/sharp/manager/';
// const title = 'http://120.79.182.43:7443/sharp/manager/';

const api={
  login: title + 'user/login',//用户登录
  changePwd: title + 'user/update_user',//修改密码

  get_all_order: title + 'order/order_list',//获取所有订单

  get_all_product: title + 'product/get_all',//获取所有商品
  update_product: title + 'product/update_product',//上架/下架商品
  get_first_category: title + 'category/get_first',//获取类目
  get_child_category:title + 'category/get_child',//获取子类目
  get_categorybrands: title + 'category/get_categorybrands',//根据类目id获取商品属性

}

export default api
