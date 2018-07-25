<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-top-text">查询条件：</div>
          <el-input class="m-top-input" v-model="searchText" size="mini" placeholder="请输入昵称或邮箱" style="width: 20%;" clearable></el-input>
          <el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>
        </div>
        <div class="m-top-button">
          <el-button class="m-top-button-button" size="mini" @click="addAdminVisible=true">添加管理员</el-button>
        </div>
      </div>
      <div class="m-middle">
        <el-table :data="adminList" stripe style="width: 100%">
          <el-table-column align="center" prop="MAid" label="编号" width="300"></el-table-column>
          <el-table-column align="center" prop="MAnicname" label="昵称" width="70"></el-table-column>
          <el-table-column align="center" prop="MAemail" label="E-mall" width="230"></el-table-column>
          <el-table-column align="center" prop="MAtelphone" label="联系方式" width="120"></el-table-column>
          <el-table-column align="center" prop="MAidentity" label="身份描述" width="120"></el-table-column>
          <el-table-column align="center" prop="MAcreatTime" label="创建时间" width="160"></el-table-column>
          <el-table-column align="center" prop="MAloginTime" label="最近登录" width="160"></el-table-column>
          <el-table-column align="center" prop="MAstatus" label="状态" width="70"></el-table-column>
          <el-table-column align="center" label="操作" fixed="right">
            <template slot-scope="scope">
              <el-button class="edit-admin-button" type="text" @click="editAdmin(scope.row)">编辑管理员</el-button>
            </template>
          </el-table-column>
        </el-table>
        <!--编辑管理员弹出框-->
        <el-dialog :title="editAdminTitle" :visible.sync="editAdminVisible" width="40%" show-close center>
          <div v-if="dialog=='index'">
            <div class="edit-dialog" style="margin-top: 0.25rem">
              <div class="change" @click="dialog='changePicture'">
                <img class="change-pictures" src="../../assets/images/changePicture.png"/>
                <div>修改管理员头像</div>
              </div>
              <div class="change" @click="dialog='changePw'">
                <img class="change-pictures" src="../../assets/images/changePw.png"/>
                <div>修改管理员密码</div>
              </div>
              <div v-if="row.MAstatus == '可用'">
                <div class="change" @click="lockAdmin('封禁')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>封禁管理员</div>
                </div>
              </div>
              <div v-if="row.MAstatus == '禁用'">
                <div class="change" @click="lockAdmin('解封')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>解封管理员</div>
                </div>
              </div>
              <div v-if="row.MAstatus == '未激活'">
                <div class="change" @click="lockAdmin('激活')">
                  <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                  <div>激活管理员</div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePicture'">
            <div class="edit-dialog" style="margin-top: 0.15rem">
              <el-upload class="avatar-uploader" action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.2rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button class="m-top-button-button" @click="dialog='index'">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePw'">
            <div class="edit-dialog">
              <el-form :model="form" style="margin-right: 0.4rem">
                <el-form-item label="请输入旧密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.oldPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
                <el-form-item label="请输入新密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.newPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
                <el-form-item label="请确认新密码：" :label-width="formLabelWidth">
                  <el-input v-model="form.againNewPw" auto-complete="off" type="password" size="mini"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.1rem">
                <el-button @click="dialog='index'" size="mini">取 消</el-button>
                <el-button class="m-top-button-button" @click="changePwDone" size="mini">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changeMAstatus'">
            <div class="edit-dialog" style="margin-top: 0.25rem;height: 1.2rem">
              <div style="text-align: center;font-size: 18px">确认{{operation}}该管理员吗？</div>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.4rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button class="m-top-button-button" @click="changeMAstatus">确 定</el-button>
              </div>
            </div>
          </div>
        </el-dialog>
        <!--添加管理员弹出框-->
        <el-dialog title="添加管理员" :visible.sync="addAdminVisible" width="30%" center>
          <div class="add-dialog">
            <el-form :model="addForm">
              <el-form-item label="用户名：" :label-width="addFormWidth">
                <el-input v-model="addForm.userName" size="mini"></el-input>
              </el-form-item>
              <el-form-item label="昵称：" :label-width="addFormWidth">
                <el-input v-model="addForm.nickName" size="mini"></el-input>
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
              <el-form-item label="状态：" :label-width="addFormWidth">
                <el-switch v-model="addForm.status" active-text="正常" inactive-text="失效">
                </el-switch>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.3rem">
              <el-button @click="addAdminVisible=false" size="mini">取 消</el-button>
              <el-button class="m-top-button-button" @click="addAdminVisible=false" size="mini">确 定</el-button>
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
        name: '管理员管理',
        inputID: '',
        inputName: '',
        adminList: [],
        editAdminVisible: false,
        addAdminVisible: false,
        editAdminTitle: '',
        dialog: '',
        imageUrl: '',
        form: {
          oldPw: '',
          newPw: '',
          againNewPw: '',
        },
        addForm: {
          userName: '',
          nickName: '',
          email: '',
          password: '',
          againPassword: '',
          status: true
        },
        formLabelWidth: '1.2rem',
        addFormWidth: '1rem',
        total_page: 0,
        current_page: 0,
        total_num: 0,
        page_size: 10,
        searchText: '',
        row: [],
        operation: '',
        MAid: ''
      }
    },
    components:{
      Pagination, pageTitle
    },
    methods: {
      // 获取管理员数据的方法
      getData(v){
        let params = {
          token: localStorage.getItem('token'),
          page_num: v || this.current_page,
          page_size: this.page_size,
          MAfilter: this.searchText
        };
        axios.get(api.get_managers, {params: params}).then(res => {
          if(res.data.status == 200) {
            this.adminList = res.data.data.Managers;
            // console.log(this.adminList)
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
          this.$message({ message: '这已经是第'+v+'页数据了', type: 'warning' });
          return false;
        }
        this.current_page = v;
        this.getData(v);
      },
      // 页面刷新的方法
      freshClick(){
        console.log('fresh');
      },
      // 头部的模糊查询
      topSearch() {
        // console.log('searchText', this.searchText);
        this.getData(1)
      },
      // 点击编辑管理员数据按钮所对应的方法
      editAdmin(row) {
        this.row = row
        this.editAdminVisible = true;
        this.dialog = 'index';
        this.editAdminTitle = row.MAid+' 管理员数据管理';
      },
      // 点击封禁、解封、激活管理员产生的Dialog变化
      lockAdmin(title) {
        this.operation = title
        this.dialog = 'changeMAstatus'
      },
      // 封禁、解封、激活管理员的方法
      changeMAstatus() {
        let that = this
        let MAstatus = ''
        if(this.row.MAstatus == '未激活' || this.row.MAstatus == '禁用') {
          MAstatus = '可用'
        }else if(this.row.MAstatus == '可用') {
          MAstatus = '禁用'
        }
        let params = {
          MAtelphone: this.row.MAtelphone,
          MAstatus: MAstatus
        }
        axios.post(api.update_manager_by_matel+'?token='+localStorage.getItem('token'), params).then(res => {
          console.log(res)
          if(res.data.status == 200){
            this.editAdminVisible = false
            this.$message({ message:res.data.message, type:'success' });
            that.getData();
          }
        })
      },
      // 更改用户头像
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      },
      // 更改密码
      changePwDone() {
        if(this.form.againNewPw != this.form.newPw) {
          this.$message.error('两次密码输入不一致！');
        }else {
          this.$message({ type: 'success', message: '操作成功!' });
          this.dialog = 'index';
        }
      }
    },
    created() {
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
          line-height: 0.25rem;
          font-size: 14px;
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
    }
    .m-top-button-button {
      background-color: @btnActiveColor;
      border-color: @btnActiveColor;
      color: @bgMainColor;
      float: right;
      font-size: 14px;
    }
    .m-middle {
      .edit-admin-button {
        color: @sidebarChildColor;
      }
      /*.el-crud {
        font-size: 14px;
        color: #000000;
      }*/
      .edit-dialog {
        .el-form-item {
          margin-bottom: 0;
        }
        // 更改用户头像
        .avatar-uploader {
          text-align: center;
        }
        .avatar-uploader .el-upload {
          border-radius: 6px;
          cursor: pointer;
          position: relative;
          overflow: hidden;
        }
        .avatar-uploader .el-upload:hover {
          border-color: #409EFF;
        }
        .avatar-uploader-icon {
          font-size: 18px;
          color: #8c939d;
          width: 0.85rem;
          height: 0.85rem;
          line-height: 0.85rem;
          text-align: center;
        }
        .avatar {
          width: 0.85rem;
          height: 0.85rem;
          display: block;
        }
        height: 1.6rem;
        .change {
          float: left;
          width: 28%;
          margin-left: 0.2rem;
          text-align: center;
          .change-pictures {
            width: 0.85rem;
            height: 0.85rem;
          }
        }
      }
      .add-dialog {
        .el-form-item {
          margin-bottom: 0;
        }
      }
    }
    .m-bottom {
      margin: 0.2rem 0.4rem 0 0;
    }
  }
</style>
