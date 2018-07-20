<template>
  <div class="m-progress-box">
    <template v-for="(item,index) in list" >
      <div class="m-progress-one " :class="item.active?'active':''">
        <p>{{item.name}}</p>
        <div class="m-progress-icon">
          <span class="m-progress-line"></span>
          <span class="m-progress-circle">{{index+1}}</span>
          <span class="m-progress-line" :class="item.next?'active':''"></span>
        </div>
        <div style="height: 0.15rem">
          <div class="time">{{item.time}}</div>
        </div>
      </div>
    </template>

  </div>

</template>

<script type="text/ecmascript-6">
  export default {
    data() {
      return {}
    },
    props:{
      list:{
        type:Array,
        default:null
      }
    },
    methods: {

    },
    created() {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
.m-progress-box{
  .flex-row(center);
  margin: 0.1rem 0.1rem 0.1rem;
  .m-progress-one{
    p{
      font-size: 0.16rem;
      line-height: 0.4rem;
      text-align: center;
      color: #b4b4b5;
    }
    .time {
      margin-top: 0.1rem;
      text-align: center;
      color: #b4b4b5;
    }
    .m-progress-icon{
      .flex-row(center);
      span{
        display: block;
        &.m-progress-line{
          width: 1.3rem;
          height: 0.05rem;
          background-color: #eeeeef;
          &.active{
            background-color: @red;
          }
        }
        &.m-progress-circle{
          width: 0.37rem;
          height: 0.37rem;
          line-height: 0.37rem;
          font-size: 0.18rem;
          color: #fff;
          border-radius: 50%;
          background-color: #eeeeef;
          text-align: center;
        }
      }
    }
    &:first-child{
      .m-progress-icon{
        span{
          &.m-progress-line{
            &:first-child{
              background-color: transparent;
              //width: 0;
            }
          }
        }
      }
    }
    &:last-child{
      .m-progress-icon{
        span{
          &.m-progress-line{
            &:last-child{
              background-color: transparent!important;
              //width: 0;
            }
          }
        }
      }
    }
    &.active{
      p{
        color: @red;
      }
      .m-progress-icon{
        span{
          &.m-progress-line{
            background-color: @red;
            &:last-child{
              background-color: #efefef;
            }
            &.active{
              background-color: @red;
            }
          }
          &.m-progress-circle{
            background-color: @red;
          }
        }
      }
    }
  }
}
</style>
