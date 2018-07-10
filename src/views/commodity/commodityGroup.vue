<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>
          <div class="m-top-text">用户ID：</div>
          <el-input class="m-top-input" v-model="inputID" size="mini"></el-input>
          <div class="m-top-text">用户名：</div>
          <el-input class="m-top-input" v-model="inputName" size="mini"></el-input>
        </div>
      </div>

      <div class="m-middle" style="width: 100%;margin-top: 0.2rem;">
        <el-table :data="user" stripe style="width: 100%">
          <el-table-column align="center" prop="userId" label="用户ID" ></el-table-column>
          <el-table-column align="center" prop="userName" label="用户名"></el-table-column>
          <el-table-column align="center" prop="email" label="时间" ></el-table-column>
          <el-table-column align="center" label="操作" >
            <template slot-scope="scope">
              <span class="m-table-edit m-table-link">编辑</span>
              <span class=" m-table-link">编辑</span>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import user from '../../common/json/userInfo'
  export default {
    data() {
      return {
        name: '用户数据管理',
        inputID: '',
        inputName: '',
        user: user
      }
    },
    components:{
      pageTitle
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
          float: left;
          background: @btnActiveColor;
          color: @bgMainColor;
          margin-right: 0.1rem;
        }
      }
      .m-top-button{
        float: right;
        .m-top-button-button {
          background: @btnActiveColor;
          color: @bgMainColor;
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
  .m-table-link{
    color: @sidebarChildColor;
    &.m-table-edit{
      padding: 0 0.2rem;
      border-right: 1px solid @borderColor;
    }
  }
</style>
