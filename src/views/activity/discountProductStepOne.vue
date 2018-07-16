<template>
  <div class="m-step">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3">基本信息</h3>
          <el-form-item label="活动名称：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
          </el-form-item>
          <el-form-item label="使用时间：">
            <el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
            <span class="m-date-line">-</span>
            <el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.date2" style="width: 2rem;"></el-date-picker>
          </el-form-item>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>面额信息——面额1</span>
            <div>
              <span class="m-step-top-edit active">+增加新面额</span>
              <span class="m-step-top-edit">-删除此面额</span>
            </div>
          </h3>
          <el-form-item label="优惠金额：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="使用门槛：">
            <span>满 &nbsp;</span>
            <el-input v-model="storeForm.name" class="m-input-special" placeholder="审批人"></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="发行量：">
            <el-input v-model="storeForm.name" class="m-input-l " placeholder="审批人"></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
          <el-form-item label="每人限额：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
        </div>
        <div class="m-bottom-btn m-flex-center">
          <router-link to="/activity/storeStepResult" >
            <span class="m-btn">创建</span>
          </router-link>

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
            name:'添加优惠券',
            active:true,
            next:false
          },
          {
            name:'完成',
            active:false,
            next:false
          }
        ],
        storeForm:{
          name:''
        }
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
