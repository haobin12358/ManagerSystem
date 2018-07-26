<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="$store.state.activity" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" >
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <el-form-item label="活动名称：" prop="ACname">
            <el-input v-model="$store.state.activity.ACname" class="m-input-l" placeholder="最多10个字" maxlength="10"></el-input>
          </el-form-item>
          <el-form-item label="活动描述：" prop="ACabo">
            <el-input v-model="$store.state.activity.ACabo" class="m-input-l" placeholder="" ></el-input>
          </el-form-item>
          <el-form-item label="活动照片:" >
            <el-upload
              action="http://120.79.182.43:7443/sharp/manager/other/upload_files"
              list-type="picture-card"
              :http-request="imgUploadTop"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :file-list="$store.state.activity.ACimage"
              class="m-img-l"
              :limit="1"
              :on-exceed="outImg">
              <span>+添加图片</span>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="image" alt="">
            </el-dialog>
            <p class="m-img-p">建议尺寸：700*700像素，最多上传1张商品图片</p>
          </el-form-item>
          <el-form-item label="优惠类型：" prop="ACbrand">
            <p>
              <el-radio v-model="$store.state.activity.ACbrand" label="1">自选商品</el-radio>
            </p>
            <p>
              <el-radio v-model="$store.state.activity.ACbrand" label="2">全店商品</el-radio>
            </p>
          </el-form-item>
          <el-form-item label="开始时间：" prop="ACstart">
            <el-date-picker type="date"  placeholder="请选择时间" v-model="$store.state.activity.ACstart" style="width: 2rem;"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束时间：" prop="ACend">
            <el-date-picker type="date"  placeholder="请选择时间" v-model="$store.state.activity.ACend" style="width: 2rem;"></el-date-picker>
          </el-form-item>

          <div class="m-bottom-btn m-flex-center">
            <router-link to="/activity/storeActivity" >
              <span class="m-btn active">返回</span>
            </router-link>
              <span class="m-btn" @click="onSubmit">下一步</span>
          </div>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  import api from  '../../api/api';
  import axios from 'axios';
  export default {
    data() {
      return {
        name:'店铺活动>创建/编辑活动',
        title_list:[
          {
            name:'店铺活动',
            url:'/activity/storeActivity'
          },
          {
            name:'创建/编辑活动',
            url:'/activity/activityStoreStepOne'
          }
        ],
        step:[
          {
            name:'基本信息',
            active:true,
            next:false
          },
          {
            name:'优惠门槛及内容',
            active:false,
            next:false
          },
          {
            name:'设置商品优惠',
            active:false,
            next:false
          }
        ],
        storeForm:{
          ACstart:'',
          ACend:'',
          ACname:'',
          ACabo:'',
          ACimage:[],
          name:''
        },
       rules:{
         ACname:[
           { required: true, message: '请输入活动名称', trigger: 'blur' }
         ],
         ACabo:[
           { required: true, message: '请输入活动描述', trigger: 'blur' }
         ],
         ACstart:[
           { required: true, message: '请选择开始时间', trigger: 'blur' }
         ],
         ACend:[
           { required: true, message: '请选择结束时间', trigger: 'blur' }
         ],
         ACbrand:[
           { required: true, message: '请选择优惠类型', trigger: 'blur' }
         ],
       },
        radio:'1',
        dialogVisible:false,
        image:''
      }
    },
    components:{
      pageTitle,
      step
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      handleRemove(file, fileList) {
        let _arr = [];
        for(let i=0;i<fileList.length;i++){
          _arr[i] = {name:fileList[i].name,url:fileList[i].url}
        }
        this.storeForm.ACimage = [].concat(_arr);
      },
      imgUploadTop(params){
        let form = new FormData();
        form.append("file", params.file);
        form.append("FileType", 'PRimage');
        form.append("contentId",  '123');
        form.append("index", 1);
        axios.post(api.upload_files,form).then(res => {
          if(res.data.status == 200){
            this.storeForm.ACimage.push({name:params.file.name,url:res.data.data});
            // this.img_index ++ ;
          }else{
            this.$message({
              type: 'error',
              message: '服务器请求失败，请稍后再试 '
            });
          }
        },error =>{
          this.$message({
            type: 'error',
            message: '服务器请求失败，请稍后再试 '
          });
        })
      },
      handlePictureCardPreview(file) {
        this.image = file.url;
        this.dialogVisible = true;
      },
      outImg(){
        this.$message({
          message: '上传图片超出数量限制',
          type: 'warning',
          duration:1000
        });
      },
      onSubmit(){
        let that = this;
        this.$refs['storeForm'].validate((valid) => {
          if (valid) {

          }
        })
          this.$router.push('/activity/activityStoreStepTwo');
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";
  .m-img-p{
    color: @greyColor;
    font-size: 0.12rem;
  }
</style>
