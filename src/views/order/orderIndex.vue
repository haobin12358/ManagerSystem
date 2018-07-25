<template>
  <div class="m-order-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="昨日" name="one">
          <order-index-top ref="one" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftOne" :leftDays="leftDays" :orderSituation="orderSituation"></order-index-left>
        </el-tab-pane>
        <el-tab-pane label="近七日" name="seven">
          <order-index-top ref="seven" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftSeven" :leftDays="leftDays" :orderSituation="orderSituation"></order-index-left>
          <my-echarts class="seven-echarts" :id="echartsId" :option="option" :width="650" :height="330"></my-echarts>
        </el-tab-pane>
        <el-tab-pane label="月度" name="thirty">
          <order-index-top ref="thirty" :days="days" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftThirty" :leftDays="leftDays" :orderSituation="orderSituation"></order-index-left>
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
        option: {}
      }
    },
    components:{
      orderIndexTop, orderIndexLeft, pageTitle, myEcharts
    },
    methods: {
      freshClick(){
        console.log('fresh');
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
            this.option = {
              title: {
                text: '近七日数据',
                subtext: '注：下单笔数不包括退单数据'
              },
              tooltip: {
                trigger: 'axis'
              },
              legend: {
                data:['下单笔数', '付款笔数']
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
                  smooth: true,
                  data: this.orderSituation.week_paying_list
                },
                {
                  name:'付款笔数',
                  type:'line',
                  smooth: true,
                  data: this.orderSituation.week_payed_list
                }
              ]
            }
            // console.log(this.orderSituation)
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      handleClick(tab, event) {
        if(tab.name == 'one') {
          this.days = '昨日';
          this.leftDays = '昨日';
          this.$refs.one.changeTopData(0);
          this.$refs.leftOne.changeLeftData(0);
        }else if(tab.name == 'seven') {
          this.days = '七日';
          this.leftDays = '上周';
          this.$refs.seven.changeTopData(1);
          this.$refs.leftSeven.changeLeftData(1);
        }else if(tab.name == 'thirty') {
          this.days = '本月';
          this.leftDays = '上月';
          this.$refs.thirty.changeTopData(2);
          this.$refs.leftThirty.changeLeftData(2);
        }
      }
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

