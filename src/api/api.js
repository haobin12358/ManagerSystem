const title = 'http://10.0.0.197:7443/sharp/manager/';
// const title = 'http://120.79.182.43:7443/sharp/manager/';

const api={
  login: title + 'user/login',//用户登录
  changePwd: title + 'user/update_user',//修改密码

  get_all_product: title + 'product/get_all',//获取所有商品

}

export default api
