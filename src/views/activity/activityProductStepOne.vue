<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <h3 class="m-step-title">查看活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <div class="m-product-step-part">
            <div>
              <el-form-item label="活动ID：">
                <span>6474987456</span>
              </el-form-item>
              <el-form-item label="活动名称：">
                <p>
                  <el-radio v-model="radio" label="1">日常活动 新品秒杀价</el-radio>
                </p>
                <p>
                  <el-radio v-model="radio" label="2">官方活动</el-radio>
                </p>
              </el-form-item>
              <el-form-item label="活动描述：">
                <el-input v-model="storeForm.name" class="m-input-xl" placeholder="限时折扣 仅限当日"></el-input>
                <p class="m-alert">活动描述仅用于商家自己管理活动，不会显示给消费者</p>
              </el-form-item>
              <el-form-item label="开始时间：">
                <el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
              </el-form-item>
              <el-form-item label="结束时间：">
                <el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
              </el-form-item>
            </div>
            <div class="m-right">
              <el-form-item label="优惠方式：">
                <p>
                  <el-radio v-model="radio" label="1">促销价</el-radio>
                </p>
                <p>
                  <el-radio v-model="radio" label="2">打折</el-radio>
                </p>
                <p>
                  <el-radio v-model="radio" label="2">满减</el-radio>
                </p>
              </el-form-item>
              <el-form-item label="活动包邮：">
                <el-switch
                  v-model="radio"
                  active-color="#9fd0bf"
                  inactive-color="#eee">
                </el-switch>
              </el-form-item>
            </div>
          </div>


          <div class="m-bottom-btn m-flex-center">
            <router-link to="/activity/productActivity" >
              <span class="m-btn active">返回</span>
            </router-link>
            <router-link to="/activity/activityProductStepTwo" >
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
        title_list:[
          {
            name:'单品活动',
            url:'/activity/productActivity'
          },
          {
            name:'创建/编辑活动',
            url:'/activity/activityProductStepOne'
          }
        ],
        step:[
          {
            name:'活动设置',
            active:true,
            next:false
          },
          {
            name:'选择活动商品',
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
  .m-alert{
    font-size: 0.12rem;
    line-height: 0.18rem;
  }
</style>
