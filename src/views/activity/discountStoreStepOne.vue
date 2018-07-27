<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3">基本信息</h3>
          <el-form-item label="活动名称：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
            <span class="m-label-line">商品范围：</span>
            <span class="m-link m-first" @click="showModal(true)">选择商品</span>
            <span class="m-remark">(已选中0商品)</span>
          </el-form-item>
          <el-form-item label="使用时间：">
            <el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>
            <span class="m-date-line">-</span>
            <el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.date2" style="width: 2rem;"></el-date-picker>
          </el-form-item>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>面额信息</span>
          </h3>
          <el-form-item label="优惠金额：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="使用门槛：">
            <span>满 &nbsp;</span>
            <el-input v-model="storeForm.name" class="m-input-special" placeholder="审批人"></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="发行量：">
            <el-input v-model="storeForm.name" class="m-input-l " placeholder="审批人"></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
          <el-form-item label="每人限额：">
            <el-input v-model="storeForm.name" class="m-input-l" placeholder="审批人"></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
        </div>
        <div class="m-bottom-btn m-flex-center">
          <router-link to="/activity/storeStepResult" >
            <span class="m-btn active">创建</span>
          </router-link>
        </div>
      </div>
    </el-form>
    <transition name="fade">
      <div class="m-modal" v-show="show_modal">
        <div class="m-modal-state">
          <div class="m-modal-head m-flex-between">
            <span>选择商品</span>
            <span class="m-close" @click="showModal(false)">X</span></div>
          <div class="m-modal-content">
            <el-form :inline="true" :model="storeForm" class="demo-form-inline">
              <div class="m-select-box">
                <div class="m-left">
                  <el-form-item label="全部类目">
                    <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                      <el-option label="区域一" value="shanghai"></el-option>
                      <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                  </el-form-item>
                  <el-form-item label="商品名称">
                    <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
                  </el-form-item>
                  <el-form-item label="商品ID">
                    <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
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
                <el-table-column type="selection" width="55"></el-table-column>
                <el-table-column align="center" prop="userId" width="400" label="宝贝描述">
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
                <el-table-column align="center" prop="userId" label="价格" ></el-table-column>

                <el-table-column align="center" prop="loginTime" label="库存" ></el-table-column>
                <!--<el-table-column align="center" label="操作" >-->
                <!--<template slot-scope="scope">-->
                <!--<span class="m-link m-first">参加活动</span>-->
                <!--</template>-->
                <!--</el-table-column>-->
              </el-table>
            </div>
            <div class="m-page-box">
              <pagination></pagination>
            </div>
          </div>
          <div class="m-modal-foot">
            <span class="m-btn active">确认</span>
            <span class="m-btn">取消</span>
          </div>
        </div>
      </div>
    </transition>
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
            name:'优惠券',
            url:'/activity/discountCoupon'
          },
          {
            name:'添加商品优惠券',
            url:'/activity/discountProductStepOne'
          }
        ],
        step:[
          {
            name:'添加优惠券',
            active:true,
            next:false
          },
          {
            name:'完成',
            active:false,
            next:false
          }
        ],
        storeForm:{
          name:''
        },
        show_modal:false,
        user:user.slice(0,1)
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
      showModal(v){
        this.show_modal = v;
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
  @import "../../common/css/modal";
</style>
