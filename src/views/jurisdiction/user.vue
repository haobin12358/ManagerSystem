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
          <el-button class="m-top-button-button" size="mini" @click="addUser">添加用户</el-button>
        </div>
      </div>

      <div class="m-middle">
        <el-table :data="user" stripe style="width: 100%">
          <el-table-column align="center" prop="userId" label="用户ID"></el-table-column>
          <el-table-column align="center" prop="userName" label="用户名"></el-table-column>
          <el-table-column align="center" prop="registerTime" label="注册时间" width="180"></el-table-column>
          <el-table-column align="center" prop="email" label="E-mall" width="180"></el-table-column>
          <el-table-column align="center" prop="group" label="用户组"></el-table-column>
          <el-table-column align="center" prop="loginTime" label="最近登录"></el-table-column>
          <el-table-column align="center" label="操作">
            <template slot-scope="scope">
              <el-dropdown size="mini" split-button>查看
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud">编辑用户权限</el-button>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud">发送密码重置邮件</el-button>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud">发送邮箱验证邮件</el-button>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud">封禁用户</el-button>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-bottom">
        <pagination></pagination>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import user from '../../common/json/userInfo'
  import Pagination from "../../components/common/pages";
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
          Pagination,
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
      .m-top-search {
        margin: 0 0 0.1rem 0;
        float: left;
        width: 85%;
        .m-top-text {
          float: left;
          line-height: 0.27rem;
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
      .m-top-button-button {
        background: @btnActiveColor;
        color: @bgMainColor;
        float: right;
      }
    }
    .m-middle {
      .el-crud {
        font-size: 0.14rem;
        color: #000000;
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0.3rem 0;
    }
  }
</style>
