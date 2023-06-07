#include<iostream>
#include<stack>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
       string ss;
       cin>>ss;
        
       stack<pair<char,int>>st;

       vector<int>vec(n,0);
      set<int>se;
      int wt=0,bl=0;
        for(int i=0;i<ss.size();i++)
        {
            if(st.empty()||st.top().first==ss[i])
            st.push({ss[i],i});
            else if(st.top().first==')'&&ss[i]=='(')
            {
                if(wt==0)
                {
                        vec[st.top().second]=1;
                     vec[i]=1;
                    se.insert(1);
                  st.pop();
                    wt=1;
                }
                else 
                {  vec[st.top().second]=2;
                  vec[i]=2;
                  se.insert(2);
                st.pop();}

                 if(wt==1&&bl==0) bl=2;
                

            }
            else if(st.top().first=='('&&ss[i]==')')
            {
                if(wt==0)
                {
                           vec[st.top().second]=1;
                          vec[i]=1;
                          se.insert(1);
                         st.pop();
                         wt=1;
                }
                else if(bl==1)
                {
                     vec[st.top().second]=1;
                  vec[i]=1;
                  se.insert(1);
                st.pop();

                }
                else
                if(wt==1&&bl==0) bl=1;
                
            }
        } 



        if(st.empty())
        {
            cout<<se.size()<<endl;
            for(int i=0;i<vec.size();i++)
            cout<<vec[i]<<" ";
            cout<<endl;
        }
        else 
        cout<<"-1"<<endl;

}
}