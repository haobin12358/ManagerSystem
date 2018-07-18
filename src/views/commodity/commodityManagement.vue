<template>
  <div class="m-user">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-search-box">
            <span class="icon icon-search"></span>
            <input type="text" placeholder="搜索">
          </div>
          <!--<div class="m-top-text">用户名：</div>-->
          <!--<el-input class="m-top-input" v-model="inputName" size="mini"></el-input>-->
          <!--<el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>-->
        </div>
        <div class="m-top-button">
          <el-button class="m-top-button-button" size="mini" @click="importProduct">发布商品</el-button>
        </div>
      </div>

      <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
        <el-table :data="product_data" stripe style="width: 100%" @selection-change="changeFun">
          <el-table-column type="selection"  width="55" ></el-table-column>
          <el-table-column align="center" prop="PRimage" label="商品" width="125">
            <template slot-scope="scope">
              <image class="m-table-img" :src="scope.row.PBimage"/>
              <!--<div class="m-table-img"></div>-->
            </template>
          </el-table-column>
          <el-table-column align="center" prop="PRname" label="名称" ></el-table-column>
          <!--<el-table-column align="center" prop="userName" label="浏览量"></el-table-column>-->
          <el-table-column align="center" prop="PRsalesvolume" label="库存" >
            <template slot-scope="scope">
              <span :class="scope.row.PRsalesvolume == 0? 'm-alert': ''">{{scope.row.PRsalesvolume}}</span>
            </template>
          </el-table-column>
          <el-table-column align="center" prop="PRsalesvolume" label="总销量" ></el-table-column>
          <el-table-column align="center" prop="PRtime" width="160" label="创建时间" ></el-table-column>
          <el-table-column align="center" prop="PRstatus" label="状态概况" :filters="[{ text: '全部', value: '全部' }, { text: '出售中', value: '出售中' },{ text: '未发布', value: '未发布' }, { text: '下架', value: '下架' }]">
            <template slot-scope="scope">
              <span :class="scope.row.PRstatus == '全部售罄'? 'm-alert': ''">{{scope.row.PRstatus}}</span>
            </template>
          </el-table-column>
          <el-table-column align="center" label="操作" >
            <template slot-scope="scope">
              <router-link to="/commodity/categorySelection" >
                <span class=" m-table-link">编辑</span>
              </router-link>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-bottom">
          <div class="m-bottom-btn-box">
            <el-button class="m-bottom-btn m-btm-cancel" size="mini" @click="soldOut">下架</el-button>
            <el-button class="m-bottom-btn " size="mini" @click="deleteProduct">删除</el-button>
          </div>
          <div class="page-button">
            <Pagination :total="total_page" @pageChange="pageChange"></Pagination>
          </div>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import { Message} from 'element-ui';
  import axios from 'axios';
  export default {
    data() {
      return {
        name: '商品管理',
        inputID: '',
        inputName: '',
        product_data: [],
        total_page:1,
        current_page:1,
        total_num:0,
        page_size:10,
        checkRow:[]
      }
    },
    components:{
      pageTitle,
      Pagination
    },
    mounted(){
      this.getData();
    },
    computed: {
      // total_page(){
      //   return Math.ceil(this.total_num / this.page_size);
      // }
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      topSearch() {
        console.log('用户ID：', this.inputID)
        console.log('用户名：', this.inputName)
      },
      changeFun(v){
        this.checkRow = v;
      },
      //发布商品
      importProduct(){
        this.updateProduct('上架状态');
      },
      //下架商品
      soldOut(){
        this.updateProduct('下架状态');
      },
      //删除商品
      deleteProduct(){
        this.updateProduct('删除状态');
      },
      updateProduct(status){
        let PRid = [];
        let that = this;
        for(let i = 0; i< this.checkRow.length;i++){
          PRid.push(this.checkRow[i].PRid);
        }
        let params = {
          PRid: PRid,
          PRstatus:status
        }
        axios.post(api.update_product+ '?token=' + this.$store.state.token,params).then(res => {
          if(res.data.status == 200){
            this.$message({
              message:res.data.message,
              type:'success',
              // duration:200000
            });
            that.getData();
          }
        })
      },
      getData(v){
        let params = {
          token:this.$store.state.token,
          PRstatus:'',
          page_num: v || this.current_page,
          page_size:this.page_size
        };
        axios.get(api.get_all_product,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.product_data = res.data.data.products;
            this.total_num = res.data.data.count;
            this.total_page = Math.ceil(this.total_num / this.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      pageChange(v){
        if(v == this.current_page){
          this.$message({
            message: '这已经是第' + v + '页数据了',
            type: 'warning'
          });
          return false;
        }
        this.current_page = v;
        this.getData(v);
      }
    },
    created() {
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background: @bgMainColor;
    .m-top {
      &:after{
        content: '';
        display: block;
        clear: both;
      }
      .m-top-search {
        margin: 0 0 0.1rem 0;
        float: left;
        .m-search-box{
          width: 1.40rem;
          height: 0.27rem;
          line-height: 0.27rem;
          font-size: 0.12rem;
          border: 1px solid @green;
          position: relative;
          border-radius: 5px;
          .icon-search{
            width: 0.18rem;
            height: 0.18rem;
            position: absolute;
            top: 0.05rem;
            left: 0.1rem;
            background: url("../../common/images/icon-search.png");
            background-size: 100% 100%;
          }
          input{
            border: none;
            height: 0.27rem;
            width: 1rem;
            padding-left: 0.4rem;
            &:focus{
              border: none;
              outline-offset: 0;
              outline-color:transparent;
            }
          }
        }
        .m-top-text {
          float: left;
          line-height: 0.27rem;
          font-size: 0.14rem;
        }
        .m-top-input {
          float: left;
          width: 12%;
          margin-right: 0.15rem;
        }
        .m-top-search-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          margin-left: 0.1rem;
        }
      }
      .m-top-button{
        float: right;
        .m-top-button-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          border-radius: 5px;
          &.active{
            background: @btnColor;
            color: @greyColor;
          }
        }
      }
    }
    .m-middle {
      /*width: 1000px;*/
      .el-crud {
        font-size: 0.14rem;
        color: #000000;
      }
    }
  }
  .m-bottom {
    margin: 0.2rem 0.4rem 0.3rem 0;
    &:after{
      content: '';
      display: block;
      clear: both;
    }
    .m-bottom-btn-box{
      float: left;
      .m-bottom-btn{
        color: #fff;
        background-color: @btnActiveColor;
        border-radius: 5px;
        &.m-btm-cancel{
          color: @greyColor;
          background-color: @btnColor;
          border: 1px solid @borderColor;
        }
      }
    }
    .page-button{
      float: right;
    }
  }
  .m-table-link{
    color: @sidebarChildColor;
    cursor: pointer;
  }
  .m-table-img{
    display: block;
    width: 1rem;
    height: 1rem;
    margin: 0.2rem 0;
    border: 1px solid @borderColor;
  }
  .m-table-num{
    color: red;
  }
  .m-alert{
    color: red;
  }
</style>
