<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-top-text">用户ID：</div>
          <el-input class="m-top-input" v-model="inputID" size="mini"></el-input>
          <div class="m-top-text">用户名：</div>
          <el-input class="m-top-input" v-model="inputName" size="mini"></el-input>
          <el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>
        </div>
        <div class="m-top-button">
          <el-button class="m-top-button-button active" size="mini" @click="addUser">全部</el-button>
          <el-button class="m-top-button-button" size="mini" @click="addUser">卖家</el-button>
          <el-button class="m-top-button-button" size="mini" @click="addUser">管理员</el-button>
        </div>
      </div>

      <div class="m-middle" style="width: 100%;margin-top: 0.2rem;">
        <el-table :data="user" stripe style="width: 100%">
          <el-table-column align="center" prop="userId" label="用户ID" ></el-table-column>
          <el-table-column align="center" prop="userName" label="用户名"></el-table-column>
          <el-table-column align="center" prop="registerTime" label="审批分类"  :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]"></el-table-column>
          <el-table-column align="center" prop="email" label="时间" ></el-table-column>
          <el-table-column align="center" prop="group" label="用户组" ></el-table-column>
          <el-table-column align="center" prop="loginTime" label="状态" :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]">
            <template slot-scope="scope">
              <span class="m-wait">已处理</span>
            </template>
          </el-table-column>
          <el-table-column align="center" label="操作" >
            <template slot-scope="scope">
              <el-button
                size="mini" class="m-table-button"
                @click="showModal(true)">详情</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-bottom">
        <pagination></pagination>
      </div>
    </div>

    <div class="m-modal" v-show="show_modal">
      <div class="m-modal-state">
        <div class="m-modal-head m-flex-between">
          <span>审批详情/活动审批</span>
        <span class="m-close" @click="showModal(false)">X</span></div>
        <div class="m-modal-content">
          <table class="m-table" width="100%">
            <thead>
            <tr>
            <td>申请人</td>
            <td>用户组</td>
            <td>状态</td>
            <td>申请时间</td>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>申请人</td>
              <td>用户组</td>
              <td>状态</td>
              <td>申请时间</td>
            </tr>
            </tbody>

          </table>
          <div class="m-approve-box">
            <p>申请详情：</p>
            <div class="m-approve-info">   申请详情xxxxx</div>
          </div>
        </div>
        <div class="m-modal-foot">
          <span class="m-btn active">通过</span>
          <span class="m-btn">否决</span>
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
        name: '管理员首页',
        inputID: '',
        inputName: '',
        user: user,
        show_modal:false
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
      },
      showModal(v){
        this.show_modal = v;
      }
    },
    created() {
      console.log(user)
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index.less";
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
          font-size: 0.14rem;
        }
      }
      .m-top-button{
        float: right;
        .m-top-button-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          font-size: 0.14rem;
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
  .m-modal{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0,0,0,0.2);
    z-index: 1001;
    .m-modal-state{
      background-color: #fff;
      padding: 0.2rem 0.4rem;
      position: absolute;
      width: 7.5rem;
      height: 4.5rem;
      top: 0;
      left: 0;
      right:0;
      bottom:0;
      margin: auto;
      border: 1px solid @borderColor;
      box-shadow: 1px 1px 2px @green;
      border-radius: 5px;
      .m-modal-head{
        border-bottom: 1px solid @borderColor;
        padding-bottom: 0.1rem;
        .m-close{
          cursor: pointer;
        }
      }
      .m-modal-content{
        padding: 0.4rem 0.2rem;
        .m-table{
          text-align: center;
          line-height: 0.6rem;
          border-radius: 5px;
          thead{
            line-height: 0.3rem;
          }
          td{
            border: 1px solid @borderColor;
          }
        }
        .m-approve-box{
          margin: 0.2rem 0 0;
          p{
            padding: 0.05rem;
            font-size: 0.14rem;
          }
          .m-approve-info{
            border: 1px solid @borderColor;
            border-radius: 10px;
            margin: 0.1rem 0;
            padding: 0.1rem;
            height: 1.2rem;
            font-size: 0.12rem;
            color: @greyColor;
          }
        }
      }
      .m-modal-foot{
        .flex-row(center);
        span.m-btn{
          display: block;
          background-color: @borderColor;
          color: @greyColor;
          padding: 0.05rem 0.3rem;
          border-radius: 5px;
          margin-left: 0.2rem;
          font-size: 0.16rem;
          cursor: pointer;
          &.active{
            background-color: @btnActiveColor;
            color: #fff;

          }
        }
      }
    }
  }
  .m-table-button{
    background-color: @sidebarChildColor;
    color: #fff;
    border-radius: 5px;
    padding: 0.05rem 0.15rem;
    &.m-cancel{
      background-color: @btnColor;
      color: @greyColor;
    }
  }
  .m-deal{
    color: @green;
  }
  .m-wait{
    color: red;
  }
  .m-bottom {
    margin: 0.2rem 0.4rem 0.3rem 0;
  }
</style>
