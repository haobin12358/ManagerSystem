<template>
  <div class="m-step">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <el-form-item label="活动名称：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
          </el-form-item>
          <el-form-item label="优惠类型：">
            <p>
              <el-radio v-model="radio" label="1">自选商品</el-radio>
            </p>
            <p>
              <el-radio v-model="radio" label="2">全店商品</el-radio>
            </p>
          </el-form-item>
          <el-form-item label="开始时间：">
            <el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束时间：">
            <el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
          </el-form-item>

          <div class="m-bottom-btn m-flex-center">
            <router-link to="/activity/storeActivity" >
              <span class="m-btn active">返回</span>
            </router-link>
            <router-link to="/activity/activityStoreStepTwo" >
              <span class="m-btn">下一步</span>
            </router-link>
          </div>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  export default {
    data() {
      return {
        name:'优惠卷>添加优惠券',
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
            name:'完成',
            active:false,
            next:false
          }
        ],
        storeForm:{
          name:'',
          date1:''
        },
        radio:'1'
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
      onSubmit(){

      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
