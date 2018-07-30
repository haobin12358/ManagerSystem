<template>
  <ul class="m-amount-sheet-ul">
    <template v-for="(item,index) in num_data">
      <li class="m-amount-sheet" :class="item.click?'active':''" @click="numListClick(index)" :style="{width:1/num_data.length*100 + '%'}">
        <p>{{item.name}}</p>
        <p class="m-num">{{item.value}}</p>
        <!--<p class="m-grey"><span>较前1日</span><span>↑</span></p>-->
      </li>
    </template>
  </ul>

</template>

<script type="text/ecmascript-6">
    export default {
        data() {
            return {
                name: ''
            }
        },
      props:{
        num_data:{
          type:Array,
          default:null
        }
      },
        components: {},
        methods: {
          numListClick(v){
            this.$emit('numListClick',v)
          }
        },
        created() {

        },
      mounted(){

      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  .m-amount-sheet-ul{
    .flex-row(flex-start);
    border: 1px solid @borderColor;
    .m-amount-sheet{
      width: 1.5rem;
      padding: 0.1rem 0.15rem;
      border-right: 1px solid @borderColor;
      cursor: pointer;
      &.active{
        border-top: 4px solid @red;
        margin-top: -2px;
      }
      &:last-child{
        border-right: none;
      }
      .m-num{
        font-size: 0.3rem;
        line-height: 0.4rem;
      }
      .m-grey{
        color: @greyColor;
        .flex-row(space-between);
        font-size: 0.12rem;
      }
    }
  }
</style>
