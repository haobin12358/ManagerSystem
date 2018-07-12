<template>
    <div class="m-step">
      <page-title :title="name" @freshClick="freshClick"></page-title>
      <div class="m-step-content">
        <div class="m-step-part">
          
        </div>
      </div>
    </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  export default {
    data() {
      return {
        name:'优惠卷>添加优惠券'
      }
    },
    components:{
      pageTitle
    },
    methods: {
      freshClick(){
        console.log('fresh');
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
