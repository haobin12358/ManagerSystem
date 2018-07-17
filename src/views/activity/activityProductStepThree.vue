<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <h3 class="m-step-title">设置商品优惠</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>活动ID：2565484102</span>
          </h3>
          <div>
            <table class="m-activity-table" width="100%">
              <tr>
                <td>活动名称：<span>新品秒杀价</span></td>
                <td >活动时间：<span>2018-06-29  00 : 00：01 至 2018-06-29  23 : 59：59</span></td>
              </tr>
              <tr>
                <td>优惠方式：<span>促销价</span></td>
                <td>活动描述：<span>限时活动 仅限当日</span></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="user" stripe style="width: 100%">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column align="center" prop="userId" width="250" label="宝贝描述">
              <template slot-scope="scope">
                <div class="m-production-description">
                  <p class="m-img"></p>
                  <div>
                    <p>商品1</p>
                    <p>ID:5489798456151241</p>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="userId" label="单价" ></el-table-column>

            <el-table-column align="center" prop="loginTime" label="库存" ></el-table-column>
            <el-table-column align="center" label="优惠方式" >
              <template slot-scope="scope">
                <p>促销价：</p>
                <el-input v-model="storeForm.name" class="m-input-xs" placeholder=""></el-input>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="userId" label="优惠后价格"></el-table-column>
            <el-table-column align="center" label="每人限购" >
              <template slot-scope="scope">
                <el-input v-model="storeForm.name" class="m-input-xs" placeholder="1"></el-input>
              </template>
            </el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-link m-first">搬出活动</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <pagination></pagination>
        </div>
        <div class="m-bottom-btn m-flex-center">
          <router-link to="/activity/activityProductStepTwo" >
            <span class="m-btn">上一步</span>
          </router-link>
          <router-link to="/activity/activityProductStepThree" >
            <span class="m-btn  active">完成</span>
          </router-link>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  export default {
    data() {
      return {
        title_list:[
          {
            name:'单品活动',
            url:'/activity/productActivity'
          },
          {
            name:'创建/编辑活动',
            url:'/activity/activityStoreStepThree'
          }
        ],
        step:[
          {
            name:'活动设置',
            active:true,
            next:true
          },
          {
            name:'选择活动商品',
            active:true,
            next:true
          },
          {
            name:'设置商品优惠',
            active:true,
            next:false
          }
        ],
        storeForm:{
          name:'',
          date1:''
        },
        radio:'1',
        user:user
      }
    },
    components:{
      pageTitle,
      step,
      Pagination
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      onSubmit(){

      },
      storeSubmit(){

      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
