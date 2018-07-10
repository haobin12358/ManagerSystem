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
          <el-button class="m-top-button-button" size="mini" @click="addAdmin">添加用户</el-button>
        </div>
      </div>

      <div class="m-middle">
        <el-table :data="admin" stripe style="width: 100%">
          <el-table-column align="center" prop="id" label="编号"></el-table-column>
          <el-table-column align="center" prop="userName" label="用户名"></el-table-column>
          <el-table-column align="center" prop="nickName" label="昵称" width="180"></el-table-column>
          <el-table-column align="center" prop="email" label="E-mall" width="180"></el-table-column>
          <el-table-column align="center" prop="group" label="用户组"></el-table-column>
          <el-table-column align="center" prop="status" label="状态"></el-table-column>
          <el-table-column align="center" label="操作">
            <template slot-scope="scope">
              <el-dropdown size="mini" split-button>查看
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud" @click="editAdmin(scope.row)">编辑管理员信息</el-button>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <el-button type="text" class="el-crud">封禁管理员</el-button>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </template>
          </el-table-column>
        </el-table>
        <el-dialog :title="editAdminTitle" :visible.sync="editAdminVisible" width="30%" show-close center>
          <div class="edit-dialog">
            <div class="change">
              <img class="change-pictures" src="../../assets/images/changePicture.png"/>
              <div>修改管理员头像</div>
            </div>
            <div class="change">
              <img class="change-pictures" src="../../assets/images/changePw.png"/>
              <div>修改管理员密码</div>
            </div>
            <div class="change">
              <img class="change-pictures" src="../../assets/images/changGroup.png"/>
              <div>设置管理员组</div>
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
  import admin from '../../common/json/adminInfo'
  import Pagination from "../../components/common/pages";
  export default {
    data() {
      return {
        name: '管理员管理',
        inputID: '',
        inputName: '',
        admin: admin,
        editAdminVisible: false,
        editAdminTitle: ''
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
      addAdmin() {
        console.log('添加用户')
      },
      editAdmin(row) {
        this.editAdminVisible = true
        this.editAdminTitle = row.id + ' 管理员数据管理'
      }
    },
    created() {
      // console.log(admin)
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
          font-size: .14rem;
        }
      }
      .m-top-button-button {
        background: @btnActiveColor;
        color: @bgMainColor;
        float: right;
        font-size: .14rem;
      }
    }
    .m-middle {
      .el-crud {
        font-size: 0.14rem;
        color: #000000;
      }
      .edit-dialog {
        height: 1.2rem;
        .change {
          float: left;
          margin-left: 0.2rem;
          text-align: center;
          .change-pictures {
            width: 0.85rem;
            height: 0.85rem;
          }
        }
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0.3rem 0;
    }
  }
</style>
