const title = 'http://10.0.0.197:7443/';
// const title = 'http://120.79.182.43:7443/';

const api={
  login: title + 'sharp/manager/user/login',//用户登录
  changePwd: title + 'sharp/manager/user/update_user',//修改密码

}

export default api
