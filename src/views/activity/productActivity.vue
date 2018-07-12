<template>
  <div class="m-discount-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
      <div class="m-discount-nav">
        <template v-for="(item,index) in tab_data" >
          <span class="m-one-nav" :class="item.show?'active':''"  @click="tabChange(item.url)">{{item.name}}</span>
        </template>
      </div>

      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.activity.show">
        <el-form :inline="true" :model="storeForm" class="demo-form-inline">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="活动状态">
                <el-select v-model="storeForm.name" class="m-input-m" placeholder="活动区域">
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="优惠券名称">
                <el-input v-model="storeForm.name" class="m-input-m" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="面额">
                <el-input v-model="storeForm.name" class="m-input-m" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="时间">
                <el-date-picker type="date" class="m-input-m" placeholder="起始时间" v-model="storeForm.date1" style="width: 1.2rem;"></el-date-picker>
              </el-form-item>
              <el-form-item label="-">
                <el-date-picker type="date" class="m-input-m" placeholder="结束时间" v-model="storeForm.date2" style="width: 1.2rem;"></el-date-picker>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
              </el-form-item>
            </div>
            <div class="m-right">
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="storeSubmit">创建</el-button>
              </el-form-item>
            </div>
          </div>
        </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="user" stripe style="width: 100%">
            <el-table-column align="center" prop="userId" label="名称/渠道"></el-table-column>
            <el-table-column align="center" prop="userId" label="状态" ></el-table-column>
            <el-table-column align="center" prop="userName" label="面额"></el-table-column>
            <el-table-column align="center" prop="group" label="门槛" ></el-table-column>
            <el-table-column align="center" prop="group" label="使用时间" >
              <template slot-scope="scope">
                <p>起：2018-07-02</p>
                <p>止：2018-07-08</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="group" label="限额" ></el-table-column>
            <el-table-column align="center" prop="loginTime" label="发行量" ></el-table-column>
            <el-table-column align="center" prop="group" label="已领取" ></el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-table-edit m-table-link">编辑</span>
                <span class=" m-table-link">推广</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <pagination></pagination>
        </div>
      </div>
      <!--商品优惠卷-->
      <div class="m-commodity" v-show="tab_data.dataInfo.show">

      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  export default {
    data() {
      return {
        name:'活动管理>单品活动',
        storeForm:{
          name:'',
          date1:'',
          date2:''
        },
        tab_data:{
          activity:{
            name:'活动管理',
            url:'activity',
            show:true
          },
          dataInfo:{
            name:'数据概况',
            url:'dataInfo',
            show:false
          }
        },
        user: user,
        option : {
          color:['#edb3b1'],
          xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisLine:{
              show:false
            }
          },
          yAxis: {
            type: 'value',
            axisLine:{
              show:false
            }
          },
          series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line'
          }]
        }

      }
    },
    components:{
      pageTitle,
      Pagination
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      storeSubmit(){

      },
      tabChange(v){
        this.tab_data[v].show = true;
        for(let item in this.tab_data){
          if(item != v){
            this.tab_data[item].show = false;
          }
        }
      }
    },
    mounted(){
      // let myChart = echarts.init(document.getElementById('echarts'));
      // myChart.setOption(this.option);
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
