// const title = 'http://10.0.0.197:7443/sharp/manager/';
// const title = 'http://120.79.182.43:7443/sharp/manager/';
const title ='http://192.168.0.100/sharp/manager/';

const api={
  login: title + 'user/login',//用户登录
  changePwd: title + 'user/update_user',//修改密码
  get_approval: title + 'approval/get_approval',//获取审批信息
  update_approval:title + 'approval/update_approval',//同意/拒绝

  get_all_order: title + 'order/order_list',//获取所有订单
  get_order_by_LOid: title + 'order/order_abo',//获取订单详情
  update_order_status: title + 'order/update_order_status',//更新订单状态

  get_managers: title + 'user/get_managers',//获取管理员列表
  get_users: title + 'user/get_users',//获取用户信息列表

  get_all_product: title + 'product/get_all',//获取所有商品
  release_product: title + 'product/release',//发布商品商品
  update_product : title + 'product/update_product',//上下架商品
  upload_files: title +'other/upload_files',//上传图片

  get_first_category: title + 'category/get_first',//获取类目
  get_child_category:title + 'category/get_child',//获取子类目
  get_categorybrands: title + 'category/get_categorybrands',//根据类目id获取商品属性
  get_category_by_prname: title + 'category/get_category_by_prname',//搜索商品对应的类目
  get_ctlist_by_ctid: title + 'category/get_ctlist_by_ctid',//根据最后一层CTid获取对应的类目
}

export default api
