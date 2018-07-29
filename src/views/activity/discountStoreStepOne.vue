<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="$store.state.discount" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" >
      <div class="m-step-content">
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3">基本信息</h3>
          <el-form-item label="活动名称：" prop="COname">
            <el-input v-model="$store.state.discount.COname" class="m-input-l" placeholder=""></el-input>
            <span class="m-label-line">商品范围：</span>
            <span class="m-link m-first" @click="showModal(true)">选择商品</span>
            <span class="m-remark">(已选中{{$store.state.discount.PRids.length}}商品)</span>
          </el-form-item>
          <el-form-item label="使用时间：" prop="COstart">
            <el-date-picker type="date"  placeholder="起始时间"  value-format="yyyy-MM-dd HH:mm:ss" v-model="$store.state.discount.COstart" style="width: 2rem;"></el-date-picker>
            <span class="m-date-line">-</span>
            <el-date-picker type="date"  placeholder="结束时间"  value-format="yyyy-MM-dd HH:mm:ss" v-model="$store.state.discount.COend" style="width: 2rem;"></el-date-picker>
          </el-form-item>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>面额信息</span>
          </h3>
          <el-form-item label="优惠金额：" prop="COamount">
            <el-input v-model="$store.state.discount.COamount" type="number" class="m-input-l" placeholder=""></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="使用门槛：" prop="COfilter">
            <span>满 &nbsp;</span>
            <el-input v-model="$store.state.discount.COfilter" type="number" class="m-input-special" placeholder=""></el-input>
            <span>&nbsp; 元</span>
          </el-form-item>
          <el-form-item label="发行量：" prop="COnumber">
            <el-input v-model="$store.state.discount.COnumber" type="number" class="m-input-l " placeholder=""></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
          <el-form-item label="每人限额：" prop="COuserfilter">
            <el-input v-model="$store.state.discount.COuserfilter" type="number" class="m-input-l" placeholder=""></el-input>
            <span>&nbsp; 张</span>
          </el-form-item>
        </div>
        <div class="m-bottom-btn m-flex-center">
          <!--<router-link to="/activity/storeStepResult" >-->
            <span class="m-btn active" @click="createOne" >创建</span>
          <!--</router-link>-->
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
                  <!--<el-form-item label="全部类目">-->
                    <!--<el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">-->
                      <!--<el-option label="区域一" value="shanghai"></el-option>-->
                      <!--<el-option label="区域二" value="beijing"></el-option>-->
                    <!--</el-select>-->
                  <!--</el-form-item>-->
                  <el-form-item label="商品名称">
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
              <el-table :data="product_data" stripe style="width: 100%" @selection-change="changeFun">
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
              <Pagination :total="page_data.total_page" @pageChange="pageChange"></Pagination>
            </div>
          </div>
          <div class="m-modal-foot">
            <span class="m-btn active" @click="onSubmit">确认</span>
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
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';
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
          name:'',
          id_list:[]
        },
        rules:{
          COname:[
            { required: true, message: '请输入活动名称', trigger: 'blur' }
          ],
          COamount:[
            { required: true, message: '请输入优惠金额', trigger: 'blur' }
          ],
          COstart:[
            { required: true, message: '请选择开始时间', trigger: 'blur' }
          ],
          COend:[
            { required: true, message: '请选择结束时间', trigger: 'blur' }
          ],
          COfilter:[
            { required: true, message: '请输入使用门槛', trigger: 'blur' }
          ],
          COnumber:[
            { required: true, message: '请输入发行量', trigger: 'blur' }
          ],
          COuserfilter:[
            { required: true, message: '请输入每人限额', trigger: 'blur' }
          ],

        },
        show_modal:false,
        product_data:[],
        page_data:{
          total_page:0,
          current_page:1,
          total_num:0,
          page_size:1
        }
      }
    },
    components:{
      pageTitle,
      step,
      Pagination
    },
    mounted(){
      this.getData()
    },
    methods: {
      /*获取表格数据*/
      getData(v,code){
        let params = {
          token:localStorage.getItem('token'),
          PBstatus:'',
          page_num: v || this.page_data.current_page,
          page_size:this.page_data.page_size,
          product_filter:code
        };
        axios.get(api.get_all_product,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.product_data = res.data.data.products;
            this.page_data.total_num = res.data.data.count;
            this.page_data.total_page = Math.ceil(this.page_data.total_num / this.page_data.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      freshClick(){
        console.log('fresh');
      },
      /*点击确认*/
      onSubmit(){
        // this.$store.state.discount.PRids = [].concat(this.storeForm.id_list);
        this.show_modal = false;
      },
      showModal(v){
        this.show_modal = v;
      },
      storeSubmit(){

      },
      /*选择商品*/
      changeFun(v){
        if(v){
          for(let i =0;i<this.storeForm.id_list.length;i++){
            if(v[0].PRid == this.storeForm.id_list[i]){
              return false;
            }
          }
          // this.storeForm.id_list.push(v[0].PRid);
        }


      },
      /*创建一个活动*/
      createOne(){
        let that = this;
        this.$refs['storeForm'].validate((valid) => {
          if (valid) {
            // console.log(this.$store.state.activity)
            let _form = JSON.parse(JSON.stringify(this.$store.state.discount));
            // for(let i =0;i<this.$store.state.activity.COimage.length;i++){
            //   _form.COimage = this.$store.state.activity.COimage[0].url
            // }
            _form.COamount = Number(_form.COamount);
            _form.COnumber = Number(_form.COnumber);
            _form.COfilter  = Number(_form.COfilter );
            _form.COdiscount = Number(_form.COdiscount);
            _form.COuserfilter = Number(_form.COuserfilter);
            axios.post(api.create+'?token='+localStorage.getItem('token'),_form).then(res => {
              if(res.data.status == 200){
                this.$router.push('/activity/storeStepResult');
                this.$message({
                  type: 'success',
                  message: '处理成功 '
                });
              }else{
                this.$message({
                  type: 'error',
                  message: '服务器请求失败，请稍后再试 '
                });
              }
            },error =>{
              this.$message({
                type: 'error',
                message: '服务器请求失败，请稍后再试 '
              });
            })

          }
        })
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
        this.getData(v)
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
