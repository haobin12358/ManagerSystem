<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
      <div class="m-step-content">
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-result">
          <div class="m-check-result-box m-flex-center">
            <i class="el-icon-circle-check m-check-icon"></i>
            <span class="m-line-height">&nbsp;创建成功！</span>
          </div>
          <div class="m-step-result-btn">
              <span @click="returnClick">返回列表</span>
          </div>
          <div class="m-discount-info">
            <h2>￥<span>{{$route.query.COamount}}</span></h2>
            <p class="m-font-14">满{{$route.query.COfilter}}元可用</p>
            <p class="m-font-12">使用时间：{{$route.query.COstart}}-{{$route.query.COend}}</p>
          </div>
        </div>
      </div>

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
            name:'优惠券',
            url:'/activity/discountCoupon'
          },
          {
            name:'添加优惠券',
            url:'/activity/storeStepResult'
          }
        ],
        step:[
          {
            name:'添加优惠券',
            active:true,
            next:true
          },
          {
            name:'完成',
            active:true,
            next:false
          }
        ]
      }
    },
    components:{
      pageTitle,
      step
    },
    mounted(){
      console.log(this.$route.query)
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      onSubmit(){

      },
      returnClick(){
        this.$router.push('/activity/discountCoupon')
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
