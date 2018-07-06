<template>
  <div class="navbar" >
    <!--<svg t="1492500959545" @click="sidebar()" class="hamburger" :class="{'is-active':isActive}" style="" viewBox="0 0 1024 1024"-->
         <!--version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1691" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24">-->
      <!--<path d="M966.8023 568.849776 57.196677 568.849776c-31.397081 0-56.850799-25.452695-56.850799-56.850799l0 0c0-31.397081 25.452695-56.849776 56.850799-56.849776l909.605623 0c31.397081 0 56.849776 25.452695 56.849776 56.849776l0 0C1023.653099 543.397081 998.200404 568.849776 966.8023 568.849776z"-->
            <!--p-id="1692"></path>-->
      <!--<path d="M966.8023 881.527125 57.196677 881.527125c-31.397081 0-56.850799-25.452695-56.850799-56.849776l0 0c0-31.397081 25.452695-56.849776 56.850799-56.849776l909.605623 0c31.397081 0 56.849776 25.452695 56.849776 56.849776l0 0C1023.653099 856.07443 998.200404 881.527125 966.8023 881.527125z"-->
            <!--p-id="1693"></path>-->
      <!--<path d="M966.8023 256.17345 57.196677 256.17345c-31.397081 0-56.850799-25.452695-56.850799-56.849776l0 0c0-31.397081 25.452695-56.850799 56.850799-56.850799l909.605623 0c31.397081 0 56.849776 25.452695 56.849776 56.850799l0 0C1023.653099 230.720755 998.200404 256.17345 966.8023 256.17345z"-->
            <!--p-id="1694"></path>-->
    <!--</svg>-->
    <div class="m-search-box">
      <span class="icon icon-search"></span>
      <input type="text" placeholder="搜索">
    </div>
    <div class="icon icon-message"></div>
    <el-dropdown :hide-on-click="false">
      <span>hello,admin<i class="icon-person-navbar icon"></i></span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>修改密码</el-dropdown-item>
        <el-dropdown-item divided>退出</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
  import store  from '../../../vuex/index.js';
export default {

  components: {

  },
  computed: {

  },
  data(){
    return{
      isActive:false
    }
  },
  methods: {
    sidebar(v){
      store.state.isCollapse = !store.state.isCollapse;
      let main = document.getElementsByClassName("main-container")[0];
      if(store.state.isCollapse){
        main.style.marginLeft = '0.63rem';
        this.isActive = true;
      }else{
        main.style.marginLeft = '1.8rem';
        this.isActive = false;
      }

    }
  }
}
</script>

<style rel="stylesheet/less" lang="less" scoped>
  @import "../../../common/css/_variate";
.navbar{
  height: 0.5rem;
  border: 1px solid @borderColor;
  display: flex;
  flex-flow: row;
  justify-content: flex-end;
  align-items: center;
  padding: 0.2rem;
  .m-search-box{
    width: 1.80rem;
    height: 0.27rem;
    line-height: 0.27rem;
    font-size: 0.12rem;
    border: 1px solid @mainColor;
    position: relative;
    border-radius: 5px;
    .icon-search{
      width: 0.18rem;
      height: 0.18rem;
      position: absolute;
      top: 0.05rem;
      left: 0.1rem;
      background: url("../../../common/images/icon-search.png");
      background-size: 100% 100%;
    }
    input{
      border: none;
      height: 0.27rem;
      width: 1.4rem;
      padding-left: 0.4rem;
      &:focus{
        border: none;
        outline-offset: 0;
        outline-color:transparent;
      }
    }
  }
  .icon{
    display: inline-block;
    width: 0.3rem;
    height: 0.3rem;
  }
  .icon-person-navbar{
      background: url("../../../common/images/icon-person-navbar.png");
    background-size: 100% 100%;
    margin: 0 0.05rem;
  }
  .icon-message{
    background: url("../../../common/images/icon-message.png");
    background-size: 100% 100%;
    margin: 0 0.2rem;
  }
  .navbar-sidebar{
    display: inline-block;
    width: 0.4rem;
    height: 0.4rem;
    cursor: pointer;
  }
}
  .hamburger.is-active {
    -webkit-transform: rotate(90deg);
    transform: rotate(90deg);
  }
  .hamburger {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }


</style>
