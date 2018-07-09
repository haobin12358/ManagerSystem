<template>
  <div class="m-user-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-left">
        <div class="one-part">

        </div>
        <div class="one-part"></div>
      </div>
      <div class="m-right">
        <div class="one-part"></div>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
    export default {
        data() {
            return {
              name:'工作模块管理'
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
.m-content{
  &:before{
    content: '';
    display: block;
    clear: both;
  }
  .m-left{
    width: 5.4rem;
    .one-part{
      background-color: #fff;
      height: 3rem;
      margin-bottom: 0.1rem;
    }
  }
  .m-right{
    width: 5.4rem;
    .one-part{
      background-color: #fff;
      height: 6.1rem;
      margin-bottom: 0.1rem;
    }
  }
}
</style>
