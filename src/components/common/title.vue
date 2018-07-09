<template>
  <div class="m-page-title">
    <span v-text="title">工作模块管理</span>
    <span class="m-page-fresh" @click="freshClick"></span>
  </div>
</template>
<script type="text/ecmascript-6">
    export default {
        data() {
            return {}
        },
        props:{
            title:{
              type:String,
              default:''
            }
        },
        methods: {
          freshClick(){
            this.$emit('freshClick');
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  .m-page-title{
    font-size: 0.14rem;
    background-color: #eeeeef;
    padding: 0.15rem;
    margin-bottom: 0.2rem;
    .flex-row(space-between);
    font-weight: 600;
    span{
      display: block;
    }
    .m-page-fresh{
      width: 0.2rem;
      height: 0.18rem;
      background: url("../../common/images/icon-fresh.png");
      background-size: 100% 100%;
      cursor: pointer;
    }
  }
</style>
