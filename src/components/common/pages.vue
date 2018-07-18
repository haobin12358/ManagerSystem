
<template>
  <div class="m-age">
    <div>
      <div class="page-total">
        记录数 {{pages}} 个
      </div>
      <div class="page-pages">
        共 {{pages}} 页
      </div>
    </div>

    <div class="page-button">
      <span @click="firstClick">首页</span>
      <el-pagination
        background
        layout="prev, pager, next"
        :total="1000"
        :pager-count="5">
      </el-pagination>
      <span @click="lastClick">尾页</span>
    </div>
  </div>
</template>

<script>
  import user from '../../common/json/userInfo'
  export default {
    name: 'Pagination',
    created:function() {
      this.sendData()
      this.setOptions()
    },
    data () {
      return {
        options: [],
        value: '',
        user: user.slice(0, 10),
        total: user.length,
        page: 1,
        pages: Math.ceil(user.length/10),
      }
    },
    methods:{
      sendData: function () {
        this.$emit('partUser', this.user)
      },
      firstPage() {
        this.page = 1
        this.user = user.slice(0, 10)
        this.sendData()
      },
      lastPage() {
        if(this.page < 2){
          console.log(this.page)
        }else {
          this.page = this.page-1
          this.user = user.slice(this.page*10-10, this.page*10)
          this.sendData()
        }
      },
      nextPage() {
        if(this.page > this.pages-1) {
          console.log(this.page)
        }else {
          this.page = this.page+1
          this.user = user.slice(this.page*10-10, this.page*10)
          this.sendData()
        }
      },
      endPage() {
        this.page = this.pages
        this.user = user.slice(this.pages*10-10, this.pages*10)
        this.sendData()
      },
      change() {
        this.page = this.value
        this.user = user.slice(this.value*10-10, this.value*10)
        this.sendData()
      },
      firstClick(){

      },
      lastClick(){

      },
      setOptions() {
        for(var i=0;i<this.pages;i++) {
          this.options.push({
            value: i+1,
            label: '第 '+(i+1)+' 页'
          })
        }
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-age{
    &:after{
      display: block;
      content: '';
      clear: both;
    }
  }
  .page-total {
    float: left;
    width: 1.15rem;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-current {
    float: left;
    width: 1.15rem;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-pages {
    float: left;
    width: 1.15rem;
    font-size: 0.14rem;
    margin: 0 0 55px 0;
  }
  .page-button {
    /*width: 4rem;*/
    float: right;
    margin-top: -10px;
    display: flex;
    flex-flow: row;
    align-items: center;
    justify-content: flex-end;
    span{
      color: @sidebarChildColor;
      cursor: pointer;
      font-size: 0.14rem;
    }
  }
  .firstPage {
    color: #000000;
  }
  .lastPage {
    color: #000000;
  }
  .nextPage {
    color: #000000;
  }
  .endPage {
    color: #000000;
  }
  .page-select {
    margin: 0 5px 0 5px;
    width: 0.93rem;
  }
</style>
