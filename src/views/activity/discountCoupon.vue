<template>
  <div class="m-discount-index">
    <page-title :title="name" :fresh="true" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
        <div class="m-discount-top">
          <div class="m-discount-top-part">
            <div class="m-top-img"></div>
            <div class="m-top-info">
              <p>优惠券</p>
              <p class="m-info-grey">可通过多种渠道推广的电子券，通过设置优惠金额和使用门槛，刺激转化提高客单，</p>
              <p class="m-info-grey">包括店铺优惠券和商品优惠券。</p>
              <p>店铺优惠券：已创建 <span class="m-num">{{page_data.total_num}}</span> 个 &nbsp;&nbsp; 平台优惠券：已创建 <span class="m-num">0</span> 个</p>
            </div>
          </div>
          <div class="m-discount-top-part">
            <router-link to="/activity/discountStoreStepOne" >
              <div class="m-top-btn">+店铺优惠券</div>
            </router-link>
            <router-link to="/activity/discountProductStepOne" >
              <div class="m-top-btn">+平台优惠券</div>
            </router-link>

          </div>
        </div>
      <tabs :tab_data="tab_data" @tabChange="tabChange"></tabs>
      <!--数据详情-->
      <div class="m-data-info" v-show="tab_data.dataInfo.show">
        <p class="m-date">
          <span>日</span>
          <el-date-picker
            v-model="situation_date"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :picker-options="pickerOptions2"
            value-format="yyyy-MM-dd HH:mm:ss"
          @change="dateChange">

          </el-date-picker>
          <!--<span class="m-date-icon"></span>-->
        </p>
        <num-list :num_data="data_detail" @numListClick="numListClick"></num-list>
        <m-echarts :width="1000" :height="300" :option="option" :id="id"></m-echarts>
      </div>

      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.store.show">
          <el-form :inline="true" :model="storeForm" class="demo-form-inline">
            <div class="m-select-box">
              <div class="m-left">
                <el-form-item label="活动状态">
                  <el-select v-model="storeForm.COstatus" class="m-input-s" placeholder="活动区域">
                    <el-option label="全部" value=""></el-option>
                    <el-option label="预热" value="预热"></el-option>
                    <el-option label="进行中" value="进行中"></el-option>
                    <el-option label="暂停" value="暂停"></el-option>
                    <el-option label="结束" value="介绍"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="优惠券名称">
                  <el-input v-model="storeForm.COname" class="m-input-s" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="类型">
                    <el-select v-model="storeForm.COstatus" class="m-input-s" placeholder="活动区域">
                      <el-option label="全部" value=""></el-option>
                      <el-option label="满减" value="满减"></el-option>
                      <el-option label="满折" value="满折"></el-option>
                      <el-option label="其它" value="其它"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="时间">
                  <el-date-picker type="date" class="m-input-s" placeholder="起始时间" value-format="yyyy-MM-dd HH:mm:ss" v-model="storeForm.COstart" style="width: 1.2rem;"></el-date-picker>
                </el-form-item>
                <el-form-item label="-">
                  <el-date-picker type="date" class="m-input-s" placeholder="结束时间" value-format="yyyy-MM-dd HH:mm:ss" v-model="storeForm.COend" style="width: 1.2rem;"></el-date-picker>
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
          <el-table :data="store_data" stripe style="width: 100%">
            <el-table-column align="center" prop="COname" label="名称/渠道"></el-table-column>
            <el-table-column align="center" prop="COstatus" label="状态" ></el-table-column>
            <el-table-column align="center" prop="COfilter" label="面额"></el-table-column>
            <el-table-column align="center" prop="COfilter" label="门槛" ></el-table-column>
            <el-table-column align="center" prop="group" label="使用时间" width="200">
              <template slot-scope="scope">
               <p>起：{{scope.row.COstart}}</p>
                <p>止：{{scope.row.COend}}</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="COuserfilter" label="每人限额" ></el-table-column>
            <el-table-column align="center" prop="COnumber" label="发行量" ></el-table-column>
            <el-table-column align="center" prop="get_num" label="已领取" ></el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-link m-first" @click="storeEdit(scope.row,'store')">查看</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <Pagination :total="page_data.total_page" @pageChange="pageChange"></Pagination>
        </div>
      </div>
      <!--商品优惠卷-->
      <div class="m-commodity" v-show="tab_data.commodity.show">
        <el-form :inline="true" :model="storeForm" class="demo-form-inline">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="活动状态">
                <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="优惠券名称">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="面额">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="时间">
                <el-date-picker type="date" class="m-input-s" placeholder="起始时间" v-model="storeForm.date1" style="width: 1.2rem;"></el-date-picker>
              </el-form-item>
              <el-form-item label="-">
                <el-date-picker type="date" class="m-input-s" placeholder="结束时间" v-model="storeForm.date2" style="width: 1.2rem;"></el-date-picker>
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
          <el-table :data="platform_data" stripe style="width: 100%">
            <el-table-column align="center" prop="userId" label="名称/渠道"></el-table-column>
            <el-table-column align="center" prop="userId" label="状态" ></el-table-column>
            <el-table-column align="center" prop="userName" label="面额"></el-table-column>
            <el-table-column align="center" prop="group" label="门槛" ></el-table-column>
            <el-table-column align="center" prop="group" label="使用时间" width="300">
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
                <span class="m-link m-first" @click="storeEdit">编辑</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <Pagination :total="page_data.total_page" @pageChange="pageChange"></Pagination>
        </div>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import tabs from '../../components/common/tabs';
  import numList from '../../components/activity/numList';
  import mEcharts from '../../components/common/vue-echarts';
  import axios from 'axios';
  import api from '../../api/api';
  export default {
    data() {
      return {
        id:'discountCoupon',
        name:'优惠券',
        storeForm:{
          COstatus:'',
          COstart:'',
          COend:'',
          COname:''
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
            name:'平台优惠券',
            url:'commodity',
            show:false
          }
        },
        data_detail:[
          {
            name:'领取张数',
            num:20,
            down_up:'down',
            click:true
          }, {
            name:'使用张数',
            num:20,
            down_up:'down',
            click:false
          }, {
            name:'优惠金额',
            num:20,
            down_up:'down',
            click:false
          },
          {
            name:'支付件数',
            num:20,
            down_up:'down',
            click:false
          },
          {
            name:'交易金额',
            num:20,
            down_up:'down',
            click:false
          }
        ],
        option : {
          color:['#edb3b1'],
          tooltip:{
            show:true,
            position: 'top',
            padding: 10,
            backgroundColor:'#edb3b1',
            textStyle:{
              color: '#fff',
              fontSize:21
            }
          },
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
        },
        option_data:[],
        pickerOptions2: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        situation_date: '',
        page_data:{
          total_page:0,
          current_page:1,
          total_num:0,
          page_size:10
        },
        store_data:[],
        platform_data:[],
    }
    },
    components:{
      pageTitle,
      Pagination,
      tabs,
      'num-list':numList,
      'm-echarts':mEcharts
    },
    methods: {
      /*获取店铺优惠券数据*/
      getStoreData(v,name,id,status,start,end,type){
        let params = {
          token:localStorage.getItem('token'),
          page_num: v || this.page_data.current_page,
          page_size:this.page_data.page_size,
          COname:name,
          COid:id,
          COstatus:status,
          COstart:start,
          COend:end,
          COtype:type,
          COgenre:'优惠券'
        };
        axios.get(api.get_all_card,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.store_data = res.data.CouponsActives;
            this.page_data.total_num = res.data.count;
            this.page_data.total_page = Math.ceil(this.page_data.total_num / this.page_data.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*获取概况*/
      getSituation() {
        axios.get(api.get_situation,{params:{
            token:localStorage.getItem('token'),
            COgenre:'优惠券',
            start_time:this.situation_date[0] || '',
            end_time:this.situation_date[1] || ''
          }}).then(res => {
          if(res.data.status == 200){
            this.data_detail = res.data.data.params;
            this.option_data = res.data.data.data;
            this.dealOption(0);
            for(let i=0;i<this.data_detail.length;i++){
              this.data_detail[i].click = false
            }
            this.data_detail[0].click = true
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*处理图*/
      dealOption(v){
        let _xAxis = [];
        let _series = [];
        for(let key in this.option_data){
          _xAxis.push(key.slice(0,11));
          _series.push(this.option_data[key][v]);
        }
        this.option.xAxis.data = [].concat(_xAxis);
        this.option.series[0].data = [].concat(_series);
      },
      /*刷新*/
      freshClick(){
        this.getStoreData();
        this.getSituation();
      },
      /*搜索*/
      storeSubmit(){
        this.getStoreData(1,this.storeForm.COname,'',this.storeForm.COstatus,this.storeForm.COstart,this.storeForm.COend,this.storeForm.COtype);
      },
      /*数据概况/店铺优惠券的切换*/
      tabChange(v){
        this.tab_data[v].show = true;
       for(let item in this.tab_data){
         if(item != v){
          this.tab_data[item].show = false;
         }
       }
      },
      /*+店铺优惠券*/
      storeEdit(v,name){
        if(name == 'store')
          this.$router.push('/activity/discountStoreStepOne?COid=' + v.COid);
      },
      /*张数点击，数据切换*/
      numListClick(v){
        let  _arr = this.data_detail;
        for(let i = 0;i<_arr.length;i++){
          _arr[i].click = false;
        }
        _arr[v].click = true;
        this.data_detail = [].concat(_arr);
        this.dealOption(v)
      },
      dateChange(){
        this.getSituation()
      },
      /*分页点击*/
      pageChange(v){
        if(v == this.current_page){
          this.$message({
            message: '这已经是第' + v + '页数据了',
            type: 'warning'
          });
          return false;
        }
        this.current_page = v;

      }
    },
    mounted(){
      this.getStoreData();
      this.getSituation();
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/activity";




</style>
