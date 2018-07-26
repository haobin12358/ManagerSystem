<template>
  <div class="m-discount-nav">
    <template v-for="(item,index) in tab_data" >
      <span class="m-one-nav" :class="item.show?'active':''"  @click="tabChange(item.url)">{{item.name}}</span>
    </template>
  </div>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
        props:{
          tab_data:{
            type:Object,
            default:null
          }
        },
        components: {},
        methods: {
          tabChange(v){
            this.$emit('tabChange',v)
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  .m-discount-nav{
    background-color: #eeeeee;
    padding: 0.1rem 0.1rem 0 0;
    margin-top: 0.1rem;
    text-align: right;
    span.m-one-nav{
      display: inline-block;
      padding: 0.02rem 0.15rem 0.05rem;
      font-size: 0.14rem;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      cursor: pointer;
      &.active{
        background-color: #fff;
      }
    }
  }
</style>
