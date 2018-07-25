<template>
  <div class="echartsBox">
    <div :id="id" :style="{width:width + 'px',height:height + 'px'}"></div>
  </div>
</template>
<script type="text/ecmascript-6">
  export default {
    props: {
      id:{
        type:String,
        default:''
      },
      width:{
        type:Number,
        default:400
      },
      height:{
        type:Number,
        default:400
      },
      option:{
        type:Object,
        default:{}
      }
    },
    data() {
      return {}
    },
    methods: {},
    created() {

    },
    mounted(){
      let myEcharts = this.echarts.init(document.getElementById(`${this.id}`))
      myEcharts.setOption(this.option)
    },
    watch:{
      'option':function (val, oldVal) {
        let myEcharts = this.echarts.init(document.getElementById(`${this.id}`))
        myEcharts.setOption(this.option)
      }
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>

</style>
