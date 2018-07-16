<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-search-box">
            <span class="icon icon-search"></span>
            <input type="text" placeholder="搜索">
          </div>
          <!--<div class="m-top-text">用户名：</div>-->
          <!--<el-input class="m-top-input" v-model="inputName" size="mini"></el-input>-->
          <!--<el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>-->
        </div>
        <div class="m-top-button">
          <el-button class="m-top-button-button" size="mini" @click="addUser">发布商品</el-button>
        </div>
      </div>

      <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
        <el-table :data="user" stripe style="width: 100%">
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column align="center" prop="userId" label="商品" width="125">
            <template slot-scope="scope">
              <!--<image class="m-table-img" src="../../common/images/icon-order.ong"/>-->
              <div class="m-table-img"></div>
            </template>
          </el-table-column>
          <el-table-column align="center" prop="userId" label="价格" >
            <template slot-scope="scope">
              <p>商品1</p>
              <p class="m-table-num">x1</p>
            </template>
          </el-table-column>
          <el-table-column align="center" prop="userName" label="浏览量"></el-table-column>
          <el-table-column align="center" prop="email" label="库存" ></el-table-column>
          <el-table-column align="center" prop="group" label="总销量" ></el-table-column>
          <el-table-column align="center" prop="group" label="创建时间" ></el-table-column>
          <el-table-column align="center" prop="loginTime" label="状态概况" :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]">
            <template slot-scope="scope">
              <span>已处理</span>
            </template>
          </el-table-column>
          <el-table-column align="center" label="操作" >
            <template slot-scope="scope">
              <router-link to="/commodity/categorySelection" >
                <span class=" m-table-link">编辑</span>
              </router-link>

            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-bottom">
          <div class="m-bottom-btn-box">
            <el-button class="m-bottom-btn m-btm-cancel" size="mini">下架</el-button>
            <el-button class="m-bottom-btn " size="mini">删除</el-button>
          </div>

          <div class="page-button">
            <el-pagination
              background
              layout="prev, pager, next"
              :total="1000">
            </el-pagination>
          </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  export default {
    data() {
      return {
        name: '商品管理',
        inputID: '',
        inputName: '',
        user: user
      }
    },
    components:{
      pageTitle,
      Pagination
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      topSearch() {
        console.log('用户ID：', this.inputID)
        console.log('用户名：', this.inputName)
      },
      addUser() {
        console.log('添加用户')
      }
    },
    created() {
      console.log(user)
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background: @bgMainColor;
    .m-top {
      &:after{
        content: '';
        display: block;
        clear: both;
      }
      .m-top-search {
        margin: 0 0 0.1rem 0;
        float: left;
        .m-search-box{
          width: 1.40rem;
          height: 0.27rem;
          line-height: 0.27rem;
          font-size: 0.12rem;
          border: 1px solid @green;
          position: relative;
          border-radius: 5px;
          .icon-search{
            width: 0.18rem;
            height: 0.18rem;
            position: absolute;
            top: 0.05rem;
            left: 0.1rem;
            background: url("../../common/images/icon-search.png");
            background-size: 100% 100%;
          }
          input{
            border: none;
            height: 0.27rem;
            width: 1rem;
            padding-left: 0.4rem;
            &:focus{
              border: none;
              outline-offset: 0;
              outline-color:transparent;
            }
          }
        }
        .m-top-text {
          float: left;
          line-height: 0.27rem;
          font-size: 0.14rem;
        }
        .m-top-input {
          float: left;
          width: 12%;
          margin-right: 0.15rem;
        }
        .m-top-search-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          margin-left: 0.1rem;
        }
      }
      .m-top-button{
        float: right;
        .m-top-button-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          border-radius: 5px;
          &.active{
            background: @btnColor;
            color: @greyColor;
          }
        }
      }
    }
    .m-middle {
      /*width: 1000px;*/
      .el-crud {
        font-size: 0.14rem;
        color: #000000;
      }
    }
  }
  .m-bottom {
    margin: 0.2rem 0.4rem 0.3rem 0;
    &:after{
      content: '';
      display: block;
      clear: both;
    }
    .m-bottom-btn-box{
      float: left;
      .m-bottom-btn{
        color: #fff;
        background-color: @btnActiveColor;
        border-radius: 5px;
        &.m-btm-cancel{
          color: @greyColor;
          background-color: @btnColor;
          border: 1px solid @borderColor;
        }
      }
    }
    .page-button{
      float: right;
    }
  }
  .m-table-link{
    color: @sidebarChildColor;
    cursor: pointer;
  }
  .m-table-img{
    display: block;
    width: 1rem;
    height: 1rem;
    margin: 0.2rem 0;
    border: 1px solid @borderColor;
  }
</style>
