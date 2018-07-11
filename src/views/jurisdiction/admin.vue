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
          <el-button class="m-top-button-button" size="mini" @click="addAdminVisible=true">添加管理员</el-button>
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
                    <el-button type="text" class="el-crud" @click="lockAdmin(scope.row)">封禁管理员</el-button>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </template>
          </el-table-column>
        </el-table>
        <el-dialog :title="editAdminTitle" :visible.sync="editAdminVisible" width="30%" show-close center>
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
              <div class="change" @click="dialog='changeGroup'">
                <img class="change-pictures" src="../../assets/images/changGroup.png"/>
                <div>设置管理员组</div>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePicture'">
            <div class="edit-dialog" style="margin-top: 0.25rem">
              <el-upload class="avatar-uploader" action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.3rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button type="primary" @click="dialog='index'">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changePw'">
            <div class="edit-dialog">
              <el-form :model="form">
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
                <el-button type="primary" @click="changePwDone" size="mini">确 定</el-button>
              </div>
            </div>
          </div>
          <div v-if="dialog=='changeGroup'">
            <div class="edit-dialog" style="margin-top: 0.25rem">
              <el-form :model="groupForm">
                <el-form-item label="活动区域" :label-width="formLabelWidth">
                  <el-select v-model="groupForm.group" placeholder="请选择分组">
                    <el-option label="管理员分组1" value="1"></el-option>
                    <el-option label="管理员分组2" value="2"></el-option>
                    <el-option label="管理员分组3" value="3"></el-option>
                    <el-option label="管理员分组4" value="4"></el-option>
                  </el-select>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer" align="right" style="margin-top: 0.6rem">
                <el-button @click="dialog='index'">取 消</el-button>
                <el-button type="primary" @click="dialog='index'">确 定</el-button>
              </div>
            </div>
          </div>
        </el-dialog>
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
              <el-button type="primary" @click="addAdminVisible=false" size="mini">确 定</el-button>
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
        addAdminVisible: false,
        editAdminTitle: '',
        dialog: '',
        imageUrl: '',
        form: {
          oldPw: '',
          newPw: '',
          againNewPw: '',
        },
        groupForm: {
          group: ''
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
      editAdmin(row) {
        this.editAdminVisible = true;
        this.dialog = 'index';
        this.editAdminTitle = row.id + ' 管理员数据管理';
      },
      lockAdmin(row) {
        this.$confirm('确认封禁编号为 ' + row.id + ' 的管理员吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          // center: true
        }).then(() => {
          this.$message({
            type: 'success',
            message: '操作成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '操作取消'
          });
        });
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
      changePwDone() {
        console.log('oldPw:', this.form.oldPw);
        console.log('newPw:', this.form.newPw);
        console.log('againNewPw:', this.form.againNewPw);
        if(this.form.againNewPw != this.form.newPw) {
          this.$message.error('两次密码输入不一致！');
        }else {
          this.dialog = 'index';
        }
      },
      created() {
        // console.log(admin);
      }
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
          line-height: 0.27rem;
          font-size: 0.14rem;
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
          font-size: .14rem;
        }
      }
      .m-top-button-button {
        background-color: @btnActiveColor;
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
          font-size: 0.18rem;
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
      margin: 0.2rem 0.4rem 0.3rem 0;
    }
  }
</style>
