<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-top-text">查询条件：</div>
          <el-input class="m-top-input" v-model="searchText" size="mini" placeholder="请输入用户名或联系方式" style="width: 20%;" clearable></el-input>
          <el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>
        </div>
        <div class="m-top-button">
          <el-button class="m-top-button-button" size="mini" @click="addUserVisible=true">添加用户</el-button>
        </div>
      </div>

      <div class="m-middle">
        <el-table :data="userList" stripe style="width: 100%">
          <el-table-column align="center" prop="USname" label="用户名"></el-table-column>
          <el-table-column align="center" prop="UStelphone" label="联系方式"></el-table-column>
          <el-table-column align="center" prop="USsex" label="性别" width="50"></el-table-column>
          <el-table-column align="center" prop="UScreateTime" label="创建时间"></el-table-column>
          <el-table-column align="center" prop="USloginTime" label="最近登录"></el-table-column>
          <el-table-column align="center" prop="USstatus" label="状态" width="70"></el-table-column>
          <el-table-column align="center" label="操作" fixed="right">
            <template slot-scope="scope">
              <div v-if="scope.row.USstatus == '禁用'">
                <el-button class="lock-user-button" type="text" @click="lockUser(scope.row, '可用')">解封</el-button>
              </div>
              <div v-if="scope.row.USstatus == '可用'">
                <el-button class="lock-user-button" type="text" @click="lockUser(scope.row, '禁用')">封禁</el-button>
              </div>
              <div v-if="scope.row.USstatus == '未激活'">
                <el-button class="lock-user-button" type="text" @click="lockUser(scope.row, '可用')">激活</el-button>
              </div>
              <!--<el-dropdown size="mini" split-button>查看
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
              </el-dropdown>-->
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
              <el-button class="add-user-done" @click="addUserVisible=false" size="mini">确 定</el-button>
            </div>
          </div>
        </el-dialog>
      </div>
      <div class="m-bottom">
        <Pagination :total="total_page" @pageChange="pageChange"></Pagination>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
    export default {
        data() {
            return {
              name: '用户数据管理',
              inputID: '',
              inputName: '',
              userList: [],
              addUserVisible: false,
              addForm: {
                userName: '',
                email: '',
                password: '',
                againPassword: '',
              },
              addFormWidth: '1rem',
              total_page: 0,
              current_page: 0,
              total_num: 0,
              page_size: 10,
              searchText: ''
            }
        },
        components:{
          Pagination, pageTitle
        },
        methods: {
          // 获取用户数据的方法
          getData(v){
            let params = {
              token: localStorage.getItem('token'),
              page_num: v || this.current_page,
              page_size: this.page_size,
              USfilter: this.searchText
            };
            axios.get(api.get_users, {params: params}).then(res => {
              if(res.data.status == 200) {
                this.userList = res.data.data.USers;
                // console.log(this.userList)
                this.total_num = res.data.data.count;
                this.total_page = Math.ceil(this.total_num / this.page_size);
              }else{
                this.$message.error(res.data.message);
              }
            },error => {
              this.$message.error(error.data.message);
            })
          },
          // 分页提示的方法
          pageChange(v){
            if(v == this.current_page){
              this.$message({
                message: '这已经是第' + v + '页数据了',
                type: 'warning'
              });
              return false;
            }
            this.current_page = v;
            this.getData(v);
          },
          // 页面刷新的方法
          freshClick(){
            console.log('fresh');
          },
          // 头部模糊查询的方法
          topSearch() {
            this.getData(1)
          },
          // 封禁、解封、激活用户的方法
          lockUser(row, USstatus) {
            console.log(row)
            this.userName = row.USname
            this.$confirm('确认'+USstatus+'用户名为 ' + this.userName + ' 的用户吗？', '提示', {
              confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning', center: true
            }).then(() => {
              let that = this
              let params = {
                UStelphone: row.UStelphone,
                USstatus: USstatus
              }
              axios.post(api.update_users+'?token='+localStorage.getItem('token'), params).then(res => {
                console.log(res)
                if(res.data.status == 200){
                  this.$message({ message:res.data.message, type:'success' });
                  that.getData();
                }
              })
            }).catch(() => {
              this.$message({ type: 'info', message: '操作取消' });
            });
          },
          // 添加用户的方法
          addUser() {
            console.log('添加用户');
          }
        },
        created() {
          // console.log(user);
          this.pageChange(1)
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
          font-size: 14px;
          line-height: 0.25rem;
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
          font-size: 14px;
        }
      }
      .m-top-button-button {
        background-color: @btnActiveColor;
        color: @bgMainColor;
        float: right;
        font-size: 14px;
      }
    }
    .m-middle {
      .lock-user-button {
        color: @sidebarChildColor;
      }
      .el-crud {
        font-size: 14px;
        color: #000000;
      }
      .add-dialog {
        margin-right: 0.4rem;
        .el-form-item {
          margin-bottom: 0;
        }
        .add-user-done {
          background-color: @btnActiveColor;
          color: @bgMainColor;
        }
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0 0;
    }
  }
</style>
