<template>
<div>
  <el-form ref="form" :model="form" label-width="80px">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <el-form-item label="活动名称">
      <el-input v-model="form.name" class="m-input-l"></el-input>
    </el-form-item>

  </el-form>
</div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
    export default {
        data() {
            return {
              name:'商品发布',
              form:{
                name:''
              }
            }
        },
      components:{
        pageTitle
      },
        methods: {
          freshClick(){
            console.log('fresh');
          },
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
.m-input-l{
  width: 4.8rem;
  height: 0.65rem;

}
</style>
