<template>
  <div class="m-user">
    <page-title :title="name" :fresh="true" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-top">
        <div class="m-top-search">
          <div class="m-top-text">申请人：</div>
          <el-input class="m-top-input" v-model="APstart" size="mini"></el-input>
          <div class="m-top-text">审批名称：</div>
          <el-input class="m-top-input" v-model="APname" size="mini"></el-input>
          <el-button class="m-top-search-button" size="mini" @click="topSearch">查询</el-button>
        </div>
        <!--<div class="m-top-button">-->
          <!--<el-button class="m-top-button-button active" size="mini" @click="addUser">全部</el-button>-->
          <!--<el-button class="m-top-button-button" size="mini" @click="addUser">卖家</el-button>-->
          <!--<el-button class="m-top-button-button" size="mini" @click="addUser">管理员</el-button>-->
        <!--</div>-->
      </div>

      <div class="m-middle" style="width: 100%;">
        <el-table :data="approval_data" stripe style="width: 100%">
          <el-table-column align="center" prop="APstart" label="申请人" ></el-table-column>
          <el-table-column align="center" prop="APname" label="审批名称"></el-table-column>
          <el-table-column align="center" prop="PEtype" label="审批分类"  :filters="[{ text: '成为卖家审批', value: '成为卖家审批' }, { text: '类目使用审批', value: '类目使用审批' },{ text: '类目增设审批', value: '类目增设审批' }, { text: '商品发布审批', value: '商品发布审批' }, { text: '活动发起审批', value: '活动发起审批' }]"></el-table-column>
          <el-table-column align="center" prop="APtime" label="时间" ></el-table-column>
          <el-table-column align="center" prop="APstatus" label="状态" :filters="[{ text: '活动发起审批', value: '活动发起审批' },{ text: '待审批', value: '待审批' }, {text: '审批中', value: '审批中' } , {text: '审批结束', value: '审批结束' } , {text: '已拒绝', value: '已拒绝' } ]">
            <template slot-scope="scope">
              <span :class="scope.row.APstatus == '待审批'? 'm-wait':''">{{scope.row.APstatus}}</span>
            </template>
          </el-table-column>
          <el-table-column align="center" label="操作" >
            <template slot-scope="scope">
              <el-button
                size="mini" class="m-table-button"
                @click="showModal(true,scope.row)">详情</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div class="m-bottom">
        <pagination :total="total_page" @pageChange="pageChange"></pagination>
      </div>
    </div>
    <transition name="fade">
      <div class="m-modal" v-show="show_modal" >
        <div class="m-modal-state">
          <div class="m-modal-head m-flex-between">
            <span>审批详情/活动审批</span>
            <span class="m-close" @click="showModal(false)">X</span></div>
          <div class="m-modal-content">
            <table class="m-table" width="100%">
              <thead>
              <tr>
                <td>申请人</td>
                <td>审批分类</td>
                <td>状态</td>
                <td>申请时间</td>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>{{row_data.APstart}}</td>
                <td>{{row_data.PEtype}}</td>
                <td>{{row_data.APstatus}}</td>
                <td>{{row_data.APtime}}</td>
              </tr>
              </tbody>

            </table>
            <div class="m-approve-box">
              <p>申请详情：</p>
              <div class="m-approve-info">   {{row_data.APremark}}</div>
            </div>
          </div>
          <div class="m-modal-foot" v-show="role && row_data.APstatus == '待审批'">
            <span class="m-btn active" @click="updateApproval('同意')">通过</span>
            <span class="m-btn" @click="updateApproval('拒绝')">否决</span>
          </div>
        </div>
      </div>
    </transition>

  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import axios from 'axios';
  import api from '../../api/api';
  export default {
    data() {
      return {
        name: '管理员首页',
        role:false,
        APname: '',
        APstart: '',
        approval_data: [],
        show_modal:false,
        row_data:{
          APstart:'',
          PEtype:'',
          APstatus:'',
          APtime:'',
          APremark:''
        },
        total_page:0,
        total_num:0,
        page_size:10

      }
    },
    components:{
      pageTitle,
      Pagination
    },
    mounted(){
      this.queryData(1);
      if(this.$store.state.role == '卖家'){
        this.name = '审批中'
      }
    },
    methods: {
      /*页面刷新*/
      freshClick(){
        this.queryData(1);
      },
      /*搜索条件搜索*/
      topSearch() {
        this.queryData(1);
      },
      /*显示详情*/
      showModal(v,row){
        this.show_modal = v;
        if(row){
          this.row_data = row;
        }
      },
      /*查询页面数据*/
      queryData(v,name,start){
        let that = this;
        axios.get(api.get_approval,{params:{
          token:localStorage.getItem('token'),
            page_size:that.page_size,
            page_num:v,
            APname:that.APname,
            APstart:that.APstart
          }}).then( res => {
          if(res.data.status == 200){
            that.approval_data = res.data.data.approvals;
            that.total_num = res.data.data.count;
            that.total_page = Math.ceil(that.total_num / that.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*审批按钮*/
      updateApproval(v){
        let that = this;
          this.$prompt('请输入'+ v +'同意理由', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消'
          }).then(({ value }) => {
            axios.post(api.update_approval +'?token=' + localStorage.getItem('token'),{
              APid:this.row_data.APid,
              APaction:v,
              APremark:value
            }).then(res => {
              if(res.data.status == 200){
                that.show_modal = false;
                that.queryData(1);
                this.$message({
                  type: 'success',
                  message: '处理成功 '
                });
              }else{
                this.$message.error(res.data.message);
              }
            },error => {
              this.$message.error(error.data.message);
            })
          }).catch(() => {
          });
      },
      /*分页点击*/
      pageChange(v){
        this.queryData(v);
      }
    },
    created() {
      if(this.$store.state.role.indexOf('管理员') != -1){
        this.role = true
      }else{
        this.role = false
      }
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index.less";
  @import "../../common/css/modal";
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
        .m-top-text {
          float: left;
          line-height: 0.27rem;
          font-size: 0.14rem;
        }
        .m-top-input {
          float: left;
          width: 1rem;
          margin-right: 0.15rem;
        }
        .m-top-search-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          margin-left: 0.1rem;
          padding: 0.03rem 0.1rem;
          font-size: 0.14rem;
          border: none;
        }
      }
      .m-top-button{
        float: right;
        .m-top-button-button {
          background: @btnActiveColor;
          color: @bgMainColor;
          font-size: 0.14rem;
          padding: 0.03rem 0.1rem;
          border: none;
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

  .m-table-button{
    background-color: @sidebarChildColor;
    color: #fff;
    border-radius: 5px;
    padding: 0.05rem 0.15rem;
    &.m-cancel{
      background-color: @btnColor;
      color: @greyColor;
    }
  }
  .m-deal{
    color: @green;
  }
  .m-wait{
    color: red;
  }
  .m-bottom {
    margin: 0.2rem 0.4rem 0.3rem 0;
  }

</style>
