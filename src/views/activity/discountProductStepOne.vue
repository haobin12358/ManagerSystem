<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" >
      <div class="m-step-content">
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3">基本信息</h3>
          <el-form-item label="活动名称：" >
            <el-input v-model="storeForm.COname" class="m-input-l" maxlength="10" placeholder="最多10个字"></el-input>
          </el-form-item>
          <el-form-item label="使用时间：" >
            <el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.COstart" style="width: 2rem;"></el-date-picker>
            <span class="m-date-line">-</span>
            <el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.COend" style="width: 2rem;"></el-date-picker>
          </el-form-item>
        </div>
        <template v-for="(item,index) in denomination_data">
          <div class="m-step-part">
            <h3 class="m-step-h3 m-flex-between">
              <span>面额信息——面额{{index + 1}}</span>
              <div>
                <span class="m-step-top-edit active" @click="addDenomination">+增加新面额</span>
                <span class="m-step-top-edit" @click="cutDenomination(index)">-删除此面额</span>
              </div>
            </h3>
            <el-form-item label="优惠金额：">
              <el-input v-model="storeForm.COamount" class="m-input-l" placeholder="审批人"></el-input>
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
        </template>

        <div class="m-bottom-btn m-flex-center">
          <router-link to="/activity/storeStepResult" >
            <span class="m-btn active">创建</span>
          </router-link>

        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  export default {
    data() {
      return {
        title_list:[
          {
            name:'优惠券',
            url:'/activity/discountCoupon'
          },
          {
            name:'添加店铺优惠券',
            url:'/activity/discountStoreStepOne'
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
        denomination_data:[1],
        storeForm:{
          COname:'',
          COstart:'',
          COend:'',
          COamount:'',
          name:''
        },
        rules:{
          COname:[
            { required: true, message: '请输入活动名称', trigger: 'blur' }
          ],
          COstart:[
            { required: true, message: '请选择开始时间', trigger: 'blur' }
          ],
          COend:[
            { required: true, message: '请选择结束时间', trigger: 'blur' }
          ],
          COamount:[
            { required: true, message: '请选择优惠金额', trigger: 'blur' }
          ],
        },
      }
    },
    components:{
      pageTitle,
      step
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      addDenomination(){
        this.denomination_data.push(1)
      },
      cutDenomination(v){
        if(this.denomination_data.length <=1 ){
          this.$message({
            type: 'warning',
            message: '默认至少一个面额'
          });
          return false;
        }
        this.$confirm('此操作将永久删除该面额, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.denomination_data.splice(v,1)
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });

      },
      onSubmit(){

      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
