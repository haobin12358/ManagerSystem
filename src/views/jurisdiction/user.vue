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
          <el-table-column prop="userId" label="用户ID" width="130"></el-table-column>
          <el-table-column prop="userName" label="用户名" width="130"></el-table-column>
          <el-table-column prop="registerTime" label="注册时间" width="180"></el-table-column>
          <el-table-column prop="email" label="E-mall" width="180"></el-table-column>
          <el-table-column prop="group" label="用户组" width="130"></el-table-column>
          <el-table-column prop="loginTime" label="最近登录" width="150"></el-table-column>
          <!--<el-table-column label="操作" width="130">-->
            <!--<template slot-scope="scope">-->
              <!--<el-dropdown size="mini" split-button type="primary" @click="openAdminForm(scope.row, 'query')">查看-->
                <!--<el-dropdown-menu slot="dropdown">-->
                  <!--<el-dropdown-item>-->
                    <!--<el-button type="text" class="el-crud" @click="lockAdmin(scope.row)">封禁管理员</el-button>-->
                  <!--</el-dropdown-item>-->
                  <!--<el-dropdown-item>-->
                    <!--<el-button type="text" class="el-crud" @click="openAdminForm(scope.row, 'edit')">编辑管理员信息</el-button>-->
                  <!--</el-dropdown-item>-->
                <!--</el-dropdown-menu>-->
              <!--</el-dropdown>-->
            <!--</template>-->
          <!--</el-table-column>-->
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
    .m-top {
      .m-top-search {
        float: left;
        width: 90%;
        padding-left: 10px;
        margin-bottom: 15px;
        .m-top-text {
          float: left;
          line-height: 24px;
          padding-left: 10px;
        }
        .m-top-input {
          float: left;
          width: 12%;
        }
        .m-top-search-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          margin-left: 10px;
        }
      }
      .m-top-button-button {
        background: @btnActiveColor;
        color: @bgMainColor;
        float: right;
      }
    }
    .m-middle {
      .el-table th {
        background: red;
        height: 35px;
      }
      .el-table td {
        padding: 2px 0;
      }
    }
  }
</style>
