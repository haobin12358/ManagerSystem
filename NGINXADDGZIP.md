# NGINX 配置GZIP 
NGINX 里配置静态文件服务器的时候，如果只是简单的小图片，那么NGINX做服务器问题不大，如果稍微打一点，甚至加上了视频，为了客户体验，加上GZIP会更加流畅一点  
参考链接  [NGINX配置gzip](https://www.cnblogs.com/itsharehome/p/7168259.html?utm_source=itdadao&utm_medium=referral)  
特别需要注意的是，类型里配置png之后会发现反而影响性能
