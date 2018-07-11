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
          <el-button class="m-top-button-button" size="mini" @click="addUserVisible=true">添加用户</el-button>
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
        <el-dialog title="添加用户" :visible.sync="addUserVisible" width="30%" center>
          <div class="add-dialog">
            <el-form :model="addForm">
              <el-form-item label="用户名：" :label-width="addFormWidth">
                <el-input v-model="addForm.userName" size="mini"></el-input>
              </el-form-item>
              <el-form-item label="邮箱：" :label-width="addFormWidth">
                <el-input v-model="addForm.email" size="mini"></el-input>
              </el-form-item>
              <el-form-item label="密码：" :label-width="addFormWidth">
                <el-input v-model="addForm.password" size="mini"></el-input>
              </el-form-item>
              <el-form-item label="确认密码：" :label-width="addFormWidth">
                <el-input v-model="addForm.againPassword" size="mini"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.2rem">
              <el-button @click="addUserVisible=false" size="mini">取 消</el-button>
              <el-button type="primary" @click="addUserVisible=false" size="mini">确 定</el-button>
            </div>
          </div>
        </el-dialog>
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
              user: user,
              addUserVisible: false,
              addForm: {
                userName: '',
                email: '',
                password: '',
                againPassword: '',
              },
              addFormWidth: '1rem'
            }
        },
        components:{
          'Pagination': Pagination,
          'pageTitle': pageTitle
        },
        methods: {
          freshClick(){
            console.log('fresh');
          },
          topSearch() {
            console.log('用户ID：', this.inputID);
            console.log('用户名：', this.inputName);
          },
          addUser() {
            console.log('添加用户');
          }
        },
        created() {
          // console.log(user);
        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background-color: @bgMainColor;
    .m-top {
      .m-top-search {
        margin: 0 0 0.1rem 0;
        float: left;
        width: 85%;
        .m-top-text {
          float: left;
          font-size: 0.14rem;
          line-height: 0.27rem;
        }
        .m-top-input {
          float: left;
          width: 12%;
          margin-right: 0.15rem;
        }
        .m-top-search-button {
          background-color: @btnActiveColor;
          color: @bgMainColor;
          margin-left: 0.1rem;
          font-size: 0.14rem;
        }
      }
      .m-top-button-button {
        background-color: @btnActiveColor;
        color: @bgMainColor;
        float: right;
        font-size: 0.14rem;
      }
    }
    .m-middle {
      .el-crud {
        font-size: 0.14rem;
        color: #000000;
      }
      .add-dialog {
        .el-form-item {
          margin-bottom: 0;
        }
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0.3rem 0;
    }
  }
</style>
