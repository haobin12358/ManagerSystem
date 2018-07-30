<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="$store.state.activity" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" :disabled="$store.state.activity.disabled">
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <el-form-item label="活动名称：" prop="COname">
            <el-input v-model="$store.state.activity.COname" class="m-input-l" placeholder="最多10个字" maxlength="10"></el-input>
          </el-form-item>
          <el-form-item label="活动描述：" prop="COabo">
            <el-input v-model="$store.state.activity.COabo" class="m-input-l" placeholder="" ></el-input>
          </el-form-item>
          <el-form-item label="活动照片:" >
            <el-upload
              action="http://120.79.182.43:7443/sharp/manager/other/upload_files"
              list-type="picture-card"
              :http-request="imgUploadTop"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :file-list="$store.state.activity.COimage"
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

          <el-form-item label="开始时间：" prop="COstart">
            <el-date-picker type="date"  placeholder="请选择时间" value-format="yyyy-MM-dd HH:mm:ss" v-model="$store.state.activity.COstart" style="width: 2rem;"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束时间：" prop="COend">
            <el-date-picker type="date"  placeholder="请选择时间" value-format="yyyy-MM-dd HH:mm:ss" v-model="$store.state.activity.COend" style="width: 2rem;"></el-date-picker>
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
          COstart:'',
          ACend:'',
          ACname:'',
          ACabo:'',
          ACimage:[],
          name:''
        },
       rules:{
         COname:[
           { required: true, message: '请输入活动名称', trigger: 'blur' }
         ],
         COabo:[
           { required: true, message: '请输入活动描述', trigger: 'blur' }
         ],
         COstart:[
           { required: true, message: '请选择开始时间', trigger: 'blur' }
         ],
         COend:[
           { required: true, message: '请选择结束时间', trigger: 'blur' }
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
    mounted(){
      if(this.$route.query.COid){
        this.getData(this.$route.query.COid);
      }
    },
    methods: {
      /*获取活动详情*/
      getData(v){
        axios.get(api.get_acabo,{
          params:{
            token:localStorage.getItem('token'),
            COid:v
          }
        }).then(res => {
          console.log(res)
          if(res.data.status == 200){
            this.$store.state.activity =  {
              COabo:res.data.data.COabo,
              COname:res.data.data.COname,
              COstatus:res.data.data.COstatus,
              COstart:res.data.data.COstart,
              COend:res.data.data.COend,
              COfilter:res.data.data.COfilter,
              COother:res.data.data.COother,
              COdiscount:res.data.data.COdiscount,
              COamount:res.data.data.COamount,
              COtype:res.data.data.COtype,
              COunit:res.data.data.COunit,
              COnumber:res.data.data.COnumber,
              COimage:res.data.data.COimage,
              COotherType:res.data.data.COotherType,
              COotherContent:[
                '','',''
              ],
              COproduct: res.data.data.PRids.length >0 ?'自选商品':'全店商品',
              PRids:res.data.data.PRids,
              COgenre:'活动',
              disabled:true
            }
            this.$store.state.activity.COotherContent[this.$store.state.activity.COotherType] = res.data.data.COother
          }
        })
      },
      freshClick(){
        console.log('fresh');
      },
      handleRemove(file, fileList) {
        let _arr = [];
        for(let i=0;i<fileList.length;i++){
          _arr[i] = {name:fileList[i].name,url:fileList[i].url}
        }
        this.$store.state.activity.COimage = [].concat(_arr);
      },
      imgUploadTop(params){
        let form = new FormData();
        form.append("file", params.file);
        form.append("FileType", 'PRimage');
        form.append("contentId",  '123');
        form.append("index", 1);
        axios.post(api.upload_files,form).then(res => {
          if(res.data.status == 200){
            this.$store.state.activity.COimage.push({name:params.file.name,url:res.data.data});
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
            this.$router.push('/activity/activityStoreStepTwo');
          }
        })
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
