<template>
  <div class="m-order-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="昨日" name="one">
          <order-index-top ref="one" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftOne" :leftDays="leftDays"></order-index-left>
        </el-tab-pane>
        <el-tab-pane label="近七日" name="seven">
          <order-index-top ref="seven" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftSeven" :leftDays="leftDays"></order-index-left>
          <my-echarts class="seven-echarts" :id="echartsId" :option="option" :width="650" :height="330"></my-echarts>
        </el-tab-pane>
        <el-tab-pane label="月度" name="thirty">
          <order-index-top ref="thirty" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftThirty" :leftDays="leftDays"></order-index-left>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import orderIndexTop from "../../components/common/order-index-top";
  import orderIndexLeft from "../../components/common/order-index-left";
  import myEcharts from "../../components/common/vue-echarts."
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
    data() {
      return {
        name: '订单概况',
        activeName: 'seven',
        days: '近七日',
        leftDays: '上周',
        echartsId: 'myEcharts',
        orderSituation: [],
        option: {
          title: {
            text: '上周数据'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data:['下单笔数','付款笔数']
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['周一','周二','周三','周四','周五','周六','周日']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name:'下单笔数',
              type:'line',
              stack: '总量',
              data:[150, 232, 201, 154, 190, 330, 410]
            },
            {
              name:'付款笔数',
              type:'line',
              stack: '总量',
              data:[820, 932, 901, 934, 1290, 1330, 1320]
            }
          ]
        }
      }
    },
    components:{
      orderIndexTop, orderIndexLeft, pageTitle, myEcharts
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      handleClick(tab, event) {
        // console.log(tab.name);
        if(tab.name == 'one') {
          this.days = '昨日';
          this.leftDays = '昨日';
          this.$refs.one.changeTopData(0);
          this.$refs.leftOne.changeLeftData(0);
        }else if(tab.name == 'seven') {
          this.days = '近七日';
          this.leftDays = '上周';
          this.$refs.seven.changeTopData(1);
          this.$refs.leftSeven.changeLeftData(1);
        }else if(tab.name == 'thirty') {
          this.days = '本月';
          this.leftDays = '上月';
          this.$refs.thirty.changeTopData(2);
          this.$refs.leftThirty.changeLeftData(2);
        }
      },
      // 获取订单概况数据
      getData(days){
        let params = {
          token: localStorage.getItem('token'),
          days: days
        };
        axios.get(api.get_order_situation, {params: params}).then(res => {
          if(res.data.status == 200) {
            this.orderSituation =res.data.data
            console.log(this.orderSituation)
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
    },
    mounted() {
      this.getData(7)
      this.$refs.seven.changeTopData(1);
      this.$refs.leftSeven.changeLeftData(1);
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background-color: @bgMainColor;
    .seven-echarts {
      width: 7rem;
      float: right;
    }
  }
</style>

