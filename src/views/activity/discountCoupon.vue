<template>
  <div class="m-discount-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
        <div class="m-discount-top">
          <div class="m-discount-top-part">
            <div class="m-top-img"></div>
            <div class="m-top-info">
              <p>优惠券</p>
              <p class="m-info-grey">可通过多种渠道推广的电子券，通过设置优惠金额和使用门槛，刺激转化提高客单，</p>
              <p class="m-info-grey">包括店铺优惠券和商品优惠券。</p>
              <p>店铺优惠券：可创建 <span class="m-num">20</span> 个 &nbsp;&nbsp; 店铺优惠券：可创建 <span class="m-num">20</span> 个</p>
            </div>
          </div>
          <div class="m-discount-top-part">
            <router-link to="/activity/discountStoreStepOne" >
              <div class="m-top-btn">+店铺优惠券</div>
            </router-link>

            <div class="m-top-btn">+商品优惠券</div>
          </div>
        </div>
      <div class="m-discount-nav">
        <template v-for="(item,index) in tab_data" >
          <span class="m-one-nav" :class="item.show?'active':''"  @click="tabChange(item.url)">{{item.name}}</span>
        </template>
      </div>
      <!--数据详情-->
      <div class="m-data-info" v-show="tab_data.dataInfo.show">
        <p class="m-date">
          <span>日（2018-07-02——2018-07-02）</span>
          <span class="m-date-icon"></span>
        </p>
        <ul class="m-amount-sheet-ul">
          <li class="m-amount-sheet">
            <p>领取张数</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
          <li class="m-amount-sheet">
            <p>使用张数</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
          <li class="m-amount-sheet">
            <p>优惠金额</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
          <li class="m-amount-sheet">
            <p>支付买家数</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
          <li class="m-amount-sheet">
            <p>支付件数</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
          <li class="m-amount-sheet active">
            <p>交易金额</p>
            <p class="m-num">20</p>
            <p class="m-grey"><span>较前1日</span><span>↑</span></p>
          </li>
        </ul>
        <div class="m-discount-echart">
          <div id="echarts"></div>
        </div>
      </div>

      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.store.show">
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
              </div>
              <div class="m-right">
                <el-form-item>
                  <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
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
      <div class="m-commodity" v-show="tab_data.commodity.show">

      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import echarts from 'echarts';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  export default {
    data() {
      return {
        name:'优惠券',
        storeForm:{
          name:'',
          date1:'',
          date2:''
        },
        tab_data:{
          dataInfo:{
            name:'数据概况',
            url:'dataInfo',
            show:true
          },
          store:{
            name:'店铺优惠劵',
            url:'store',
            show:false
          },
          commodity:{
            name:'商品优惠券',
            url:'commodity',
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
      let myChart = echarts.init(document.getElementById('echarts'));
      myChart.setOption(this.option);
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/activity";




</style>
