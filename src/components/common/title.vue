<template>
  <div>
    <div class="m-page-title" v-if="list">
      <div>
        <template v-for="(item,index) in list" >
          <span v-if="index >0 ">&nbsp; > </span>
          <span v-text="item.name" class="m-router-link" @click="routerClick(item.url)">工作模块管理</span>
        </template>
      </div>
      <span class="m-page-fresh" @click="freshClick" v-if="fresh"></span>
    </div>

    <div class="m-page-title" v-else>
      <span v-text="title">工作模块管理</span>
      <span class="m-page-fresh" @click="freshClick" v-if="fresh"></span>
    </div>
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
            },
            list:{
              type:Array,
              default:null
            },
            fresh:{
              type:Boolean,
              default:false
            }
        },
        methods: {
          freshClick(){
            this.$emit('freshClick');
          },
          routerClick(v){
            this.$router.push(v);
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
    padding: 0.1rem 0.4rem;
    .flex-row(space-between);
    font-weight: 600;
    span{
      display: inline-block;
      &.m-router-link{
        cursor: pointer;
      }
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
