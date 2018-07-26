<template>
  <div class="m-order-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="昨日" name="one" :lazy="lazyStatus">
          <order-index-top ref="one" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftOne" :orderSituation="orderSituation"></order-index-left>
          <my-echarts class="my-echarts" id="echartsId1" :option="option1" :width="650" :height="250"></my-echarts>
        </el-tab-pane>
        <el-tab-pane label="近七日" name="seven" :lazy="lazyStatus">
          <order-index-top ref="seven" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftSeven" :orderSituation="orderSituation"></order-index-left>
          <my-echarts class="my-echarts" id="echartsId7" :option="option7" :width="650" :height="250"></my-echarts>
        </el-tab-pane>
        <el-tab-pane label="近三十日" name="thirty" :lazy="lazyStatus">
          <order-index-top ref="thirty" :orderSituation="orderSituation"></order-index-top>
          <order-index-left ref="leftThirty" :orderSituation="orderSituation"></order-index-left>
          <my-echarts class="my-echarts" id="echartsId30" :option="option30" :width="750" :height="250"></my-echarts>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import orderIndexTop from "../../components/common/order-index-top";
  import orderIndexLeft from "../../components/common/order-index-left";
  import myEcharts from "../../components/common/vue-echarts"
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
    data() {
      return {
        name: '订单概况',
        activeName: 'seven',
        days: '近七日',
        leftDays: '近七日',
        echartsId: 'myEcharts',
        orderSituation: [],
        option1: {},
        option7: {},
        option30: {},
        lazyStatus: true
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
        }
        let daysList = []
        for(let i=1;i<31;i++) {
          let day = '第'+i+'天'
          daysList.push(day)
        }
        axios.get(api.get_order_situation, {params: params}).then(res => {
          if(res.data.status == 200) {
            this.orderSituation =res.data.data
            if(days == 1) {
              this.option1 = {
                title : {
                  text: '昨日数据',
                  x:'center'
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'left',
                  data: ['未支付','已支付']
                },
                series : [
                  {
                    name: '访问来源',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    color: ['#EEB5B3', '#A0D1C1'],
                    data:[
                      { value:this.orderSituation.paying_count, name:'未支付' },
                      { value:this.orderSituation.week_paying_list[0], name:'已支付' }
                    ],
                    itemStyle: {
                      emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                      }
                    }
                  }
                ]
              }
            }else if(days == 7) {
              this.option7 = {
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
                    color: '#EEB5B3',
                    data: this.orderSituation.week_payed_list
                  },
                  {
                    name:'付款笔数',
                    type:'line',
                    smooth: true,
                    color: '#A0D1C1',
                    data: this.orderSituation.week_paying_list
                  }
                ]
              }
            }else if(days == 30) {
              this.option30 = {
                title: {
                  text: '近三十日数据',
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
                  data: daysList
                },
                yAxis: {
                  type: 'value'
                },
                series: [
                  {
                    name:'下单笔数',
                    type:'line',
                    smooth: true,
                    color: '#EEB5B3',
                    data: this.orderSituation.week_payed_list
                  },
                  {
                    name:'付款笔数',
                    type:'line',
                    smooth: true,
                    color: '#A0D1C1',
                    data: this.orderSituation.week_paying_list
                  }
                ]
              }
            }
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 判断点击的tab
      handleClick(tab, event) {
        if(tab.name == 'one') {
          this.days = '昨日'
          this.leftDays = '昨日'
          this.getData(1)
        }else if(tab.name == 'seven') {
          this.days = '七日'
          this.leftDays = '近七日'
          this.getData(7)
        }else if(tab.name == 'thirty') {
          this.days = '近三十日'
          this.leftDays = '近三十日'
          this.getData(30)
        }
      }
    },
    mounted() {
      this.getData(7)
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background-color: @bgMainColor;
    .my-echarts {
      width: 70%;
      float: left;
      margin-left: 5%;
    }
  }
</style>

