<template>
  <div class="login-status">
    <login-head></login-head>
    <div class="login-content">
      <div class="login-box">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm"  >
          <h3 class="login-head">用户登录</h3>
          <el-form-item  prop="name">
            <i class="icon-person icon"></i>
            <el-input v-model="ruleForm.MAname" class="m-input"></el-input>
          </el-form-item>
          <el-form-item  prop="pwd">
            <span class="icon-pwd icon"></span>
            <el-input v-model="ruleForm.MApassword" type="password" class="m-input"></el-input>
            <!--<i class="icon-pwd icon-r"></i>-->
          </el-form-item>
          <!--<el-form-item  prop="pwd">-->
            <!--<span class="icon-pwd icon"></span>-->
            <!--<el-input v-model="ruleForm.pwd" type="password" class="m-input"></el-input>-->
            <!--&lt;!&ndash;<i class="icon-pwd icon-r"></i>&ndash;&gt;-->
          <!--</el-form-item>-->
          <el-form-item class="m-btn">
            <el-button type="primary" @click="submitForm('ruleForm')">登 &nbsp;&nbsp;录</el-button>
          </el-form-item>
          <el-form-item >
            <el-checkbox  name="type">记住密码</el-checkbox>
            <p class="m-forget-pwd">忘记密码？</p>
          </el-form-item>
        </el-form>
      </div>
    </div>

    <foot></foot>
  </div>

</template>

<script>
  import loginHead from '../../components/common/header';
  import foot from '../../components/common/footer';
  import api from '../../api/api';
  import { MessageBox } from 'element-ui';
  import axios from 'axios';
  export default {
    components:{
      loginHead,
      foot
    },
    data() {
      return {
        ruleForm: {
          MAname: '',
          MApassword:''
        },
        rules: {
          MAname: [
            { required: true, message: '请输入账号名称', trigger: 'blur' }
          ],
          MApassword:'password',
        }
      };
    },
    methods: {
      submitForm(formName) {
        let that = this;
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.post(api.login,that.ruleForm).
            then(res=>{
              if(res.data.status == 200){
                this.$store.state.side = res.data.data.side;
                this.$store.state.role = res.data.data.MAidentity;
                if(res.data.data.MAidentity.indexOf('管理员') != -1){
                  this.$router.push({ path: '/index/adminIndex' });
                }else{
                  this.$router.push({ path: '/index/userIndex' });
                }
              }else{
                MessageBox({
                  title:'提示',
                  message:res.data.message,
                  callback: action => {

                  }
                })
              }
            }, res=>{
              MessageBox({
                title:'提示',
                message:res.data.message,
                callback: action => {

                }
              })
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
.login-status{
  height: 100%;
  .login-content{
    position: fixed;
    background-color: @mainColor;
    width: 100%;
    height: 100%;
    .login-box{
      width: 3.6rem;
       height: 4.2rem;
      padding: 0.2rem;
      position: absolute;
      top: 40%;
      right: 2.2rem;
      background-color: #fff;
      -webkit-transform: translate(0, -1.6rem);
      transform: translate(0,-1.6rem);
      border-radius: 5px;
      .login-head{
        margin-bottom: 0.4rem;
        font-size: 0.25rem;
        color: @mainColor;
      }
      .el-form-item{
        vertical-align: middle;
        position: relative;
        /*height: 0.4rem;*/
        .icon{
          width: 0.25rem;
          height: 0.25rem;
          position: absolute;
          display: inline-block;
          top:0.145rem;
          left: 0.2rem;
          z-index: 100;
        }
        .icon-person{
          background: url("../../common/images/person.png");
          background-size: 100% 100%;
        }
        .icon-r{
          width: 0.2rem;
          height: 0.2rem;
          position: absolute;
          display: inline-block;
          top:0.185rem;
          right: 0.1rem;
          z-index: 100;
        }
        .icon-pwd{
          background: url("../../common/images/pwd.png") no-repeat ;
          background-size: 100% 100%;
        }
        button{
          width: 3.6rem;
          height: 0.54rem;
          text-align: center;
          font-size: 0.2rem;
          background-color: @btnActiveColor;
          border-color: @btnActiveColor;
          margin-top: 1rem;

        }
        .m-forget-pwd{
          color: @greyColor;
          /*display: inline-block;*/
          position: absolute;
          top:0;
          right: 0;
          cursor: pointer;
        }
      }
    }
  }

}


</style>
