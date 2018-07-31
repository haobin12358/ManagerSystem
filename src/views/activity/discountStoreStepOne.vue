<template>
  <div class="m-step">
    <page-title :list="title_list" ></page-title>
    <el-form  :model="$store.state.discount" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" :disabled="$store.state.discount.disable" >
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
            <span class="m-remark">(已选中{{$store.state.discount.PRids.length}}商品,不如则默认全店商品可用)</span>
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
          <el-form :inline="true" :model="storeForm" class="demo-form-inline" :disabled="$store.state.discount.disable" >
            <div class="m-modal-head m-flex-between">
              <span>选择商品</span>
              <span class="m-close" @click="showModal(false)">X</span></div>
            <div class="m-modal-content">

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

              <div class="m-middle" style="width: 100%;margin-top: 0.1rem;" >
                <el-table :data="product_data" stripe style="width: 100%" ref="table" @selection-change="changeFun" >
                  <el-table-column type="selection" width="55" prop="COcheck" ></el-table-column>
                  <el-table-column align="center" prop="userId" width="400" label="宝贝描述">
                    <template slot-scope="scope">
                      <div class="m-production-description">
                        <img class="m-img" :src="scope.row.PRimage[0]" style="width: 0.5rem;height: 0.5rem;"/>
                        <div>
                          <p>{{scope.row.PRname}}</p>
                          <p>{{scope.row.PRid}}</p>
                        </div>
                      </div>
                    </template>
                  </el-table-column>
                  <el-table-column align="center" prop="userId" label="价格" ></el-table-column>

                  <el-table-column align="center" prop="PRstock" label="库存" ></el-table-column>
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
          </el-form>
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
          name:''
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
        },
        check_data:[]
      }
    },
    components:{
      pageTitle,
      step,
      Pagination
    },
    mounted(){
      this.getData();
      if(this.$route.query.COid){
        this.getDetailData(this.$route.query.COid);
      }
    },
    methods: {
      /*获取活动详情*/
      getDetailData(v){
        axios.get(api.get_acabo,{
          params:{
            token:localStorage.getItem('token'),
            COid:v
          }
        }).then(res => {
          if(res.data.status == 200){
            this.$store.state.discount={
              COabo:res.data.data.COabo,
              COname:res.data.data.COname,
              COstatus:res.data.data.COstatus,
              COstart:res.data.data.COstart,
              COend:res.data.data.COend,
              COfilter:res.data.data.COfilter,
              COother:res.data.data.COother,
              COdiscount:res.data.data.COdiscount,
              COamount:res.data.data.COamount,
              COtype:res.data.data.COtype,
              COunit:res.data.data.COunit,
              COnumber:res.data.data.COnumber,
              PRids:res.data.data.PRids,
              COuserfilter:res.data.data.COuserfilter,
              COgenre:'优惠券',
              disable:true
            }
          }
        })
      },
      /*获取表格数据*/
      getData(v,code){
        let that = this;
        let params = {
          token:localStorage.getItem('token'),
          page_num: v || this.page_data.current_page,
          page_size:this.page_data.page_size,
          product_filter:code
        };
        axios.get(api.get_all_product,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.product_data = res.data.data.products;
            for(let i=0;i<this.product_data.length;i++){
              if(this.$store.state.discount.PRids.indexOf(this.product_data[i].PRid)!= -1){
                that.$nextTick(function(){//注意这个，延时执行。
                  that.$refs.table.toggleRowSelection(that.product_data[i],true);//每次更新了数据，触发这个函数即可。
                });
              }
            }
            this.page_data.total_num = res.data.data.count;
            this.page_data.total_page = Math.ceil(this.page_data.total_num / this.page_data.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*点击确认*/
      onSubmit(){

        this.show_modal = false;
      },
      /*显示模态框*/
      showModal(v){
        this.show_modal = v;
      },
      /*商品查询*/
      storeSubmit(){
        this.getData(1,this.storeForm.name);
      },
      /*选择商品*/
      changeFun(e){
        let _arr = [];
        for(let i=0;i<e.length;i++){
          _arr.push(e[i].PRid);
        }
        this.check_data[this.page_data.current_page-1] = [].concat(_arr);
        let newarr=[];
        let arr = JSON.parse(JSON.stringify(this.check_data));
        for(let i=0;i<arr.length;i++)
        {
          newarr=newarr.concat(arr[i]);
        }
        this.$store.state.discount.PRids = [].concat(newarr);
      },
      /*创建一个优惠券*/
      createOne(){
        if(this.$route.query.COid){
          this.$message({
            type: 'warning',
            message: '已创建过的优惠券不可修改'
          });
          return false;
        }
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
                this.$message({
                  type: 'success',
                  message: '处理成功 '
                });
                this.$store.state.discount = {
                  COabo:'',
                  COname:'',
                  COstatus:'',
                  COstart:'',
                  COend:'',
                  COfilter:null,
                  COother:'',
                  COdiscount:null,
                  COamount:null,
                  COtype:'',
                  COnumber:null,
                  PRids:[],
                  COuserfilter:null,
                  COgenre:'优惠券'
                }
                if(this.$route.query.router == 'activity'){
                  this.$router.push('/activity/activityStoreStepTwo?COid='+res.data.data);
                }else{
                  this.$router.push({path:'/activity/storeStepResult',query:{
                      COamount:_form.COamount,
                      COfilter:_form.COfilter,
                      COstart:_form.COstart,
                      COend:_form.COend
                    }});
                }
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
        if(v == this.page_data.current_page){
          this.$message({
            message: '这已经是第' + v + '页数据了',
            type: 'warning'
          });
          return false;
        }
        this.page_data.current_page = v;
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
