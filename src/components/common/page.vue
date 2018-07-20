
<template>
  <div class="m-age" v-if="total != 0">
    <div v-if="num">
      <div class="page-total">
        记录数 {{num}} 个
      </div>
      <div class="page-pages">
        共 {{total}} 页
      </div>
    </div>

    <div class="page-button">
      <span @click="change(1)">首页</span>
      <el-pagination
        background
        layout="prev, pager, next"
        :pager-count="5"
        :page-count="total"
      @current-change="change">
      </el-pagination>
      <span @click="change(total)">尾页</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Pagination',

    data () {
      return {

      }
    },
    props:{
      total:{
        type:Number,
        default:1
      },
      num:{
        type:Number,
        default:0
      },
      page_size:{
        type:Number,
        default:10
      }
    },
    methods:{
      change(v) {
        this.$emit('pageChange',v)
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-age{
    &:after{
      display: block;
      content: '';
      clear: both;
    }
  }
  .page-total {
    float: left;
    width: 1.15rem;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-current {
    float: left;
    width: 1.15rem;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-pages {
    float: left;
    width: 1.15rem;
    font-size: 0.14rem;
    margin: 0 0 55px 0;
  }
  .page-button {
    width: 4rem;
    float: right;
    margin-top: -10px;
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: flex-end;
    span{
      color: @sidebarChildColor;
      cursor: pointer;
      font-size: 0.14rem;
    }
  }
  .firstPage {
    color: #000000;
  }
  .lastPage {
    color: #000000;
  }
  .nextPage {
    color: #000000;
  }
  .endPage {
    color: #000000;
  }
  .page-select {
    margin: 0 5px 0 5px;
    width: 0.93rem;
  }
</style>
