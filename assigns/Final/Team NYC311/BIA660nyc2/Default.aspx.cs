using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.Configuration;
using System.Data.Odbc;
using System.Data.SqlClient;

public partial class _Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string connectionString = WebConfigurationManager.ConnectionStrings["procyk01ConnectionString"].ConnectionString;
        string sql = "select distinct neighborhood from procyk01.complaints";
        OdbcConnection con = new OdbcConnection(connectionString);
        OdbcCommand cmdO = new OdbcCommand(sql, con);

        // Load List Box 1 and 2 from the same dataset (static once it's loaded)
        // If it's not a postback, don't run the following code.

        if (!Page.IsPostBack)
            try
            {
                con.Open();

                OdbcDataReader reader1 = cmdO.ExecuteReader();
                ListBox1.DataSource = reader1;
                ListBox1.DataTextField = "neighborhood";
                ListBox1.DataValueField = "neighborhood";
                ListBox1.DataBind();
                reader1.Close();

                OdbcDataReader reader2 = cmdO.ExecuteReader();
                ListBox2.DataSource = reader2;
                ListBox2.DataTextField = "neighborhood";
                ListBox2.DataValueField = "neighborhood";
                ListBox2.DataBind();
                reader2.Close();

                string initLocation1 = "Upper East Side";
                string initLocation2 = "Upper West Side";

                FillAllChartsAndGrids("2013-01-01", initLocation1, initLocation2);
            }
        finally
        {
            con.Close();
        }
    }


    protected void Button1_Click(object sender, EventArgs e)
    {
        string dt1 = DropDownList2.SelectedValue + "-";
        string dt2 = DropDownList1.SelectedValue + "-01";
        TextBox1.Text = dt1 + dt2;
        
        string QueryDate = TextBox1.Text;
        
        // defaults if user doesn't choose anything from the listboxes
        //
        string InitLocation1 ;
        if (ListBox1.SelectedValue=="")
            InitLocation1 = "Upper East Side";
        else
            InitLocation1 = ListBox1.SelectedValue;

        string InitLocation2;
        if (ListBox2.SelectedValue == "")
            InitLocation2 = "Upper West Side";
        else
            InitLocation2 = ListBox2.SelectedValue;

        FillAllChartsAndGrids(QueryDate, InitLocation1, InitLocation2);
    }


    private void FillAllChartsAndGrids(string QueryDate,string QueryLocation1,string QueryLocation2)
    {
        string connectionString = WebConfigurationManager.ConnectionStrings["procyk01ConnectionString"].ConnectionString;

        try
        {
            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            string sql = "SELECT complaint, CT ";
            sql += "FROM complaints ";
            sql += "WHERE (complaintdate = '" + QueryDate + "') AND (neighborhood = '" + QueryLocation1 + "') ";

            if (CheckBox1.Checked == true)
            {
                sql += "AND complaint NOT IN ('GENERAL CONSTRUCTION', 'NONCONST', 'PAINT - PLASTER', 'PLUMBING', 'ELECTRIC', 'HEATING') ";
            };

            sql += "ORDER BY CT DESC LIMIT 10";

            OdbcConnection con1 = new OdbcConnection(connectionString);
            OdbcCommand cmdO = new OdbcCommand(sql, con1);
            con1.Open();
            OdbcDataReader reader1 = cmdO.ExecuteReader();
            Chart1.DataSource = reader1;
            Chart1.DataBind();

            Chart1.Series["Series1"].ToolTip = "#VALX\nCount: #VALY";

            reader1.Close();
            con1.Close();

            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            string sql2 = "SELECT complaint, CT ";
            sql2 += "FROM complaints ";
            sql2 += "WHERE (complaintdate = '" + QueryDate + "') AND (neighborhood = '" + QueryLocation2 + "') ";

            if (CheckBox2.Checked == true)
            {
                sql2 += "AND complaint NOT IN ('GENERAL CONSTRUCTION', 'NONCONST', 'PAINT - PLASTER', 'PLUMBING', 'ELECTRIC', 'HEATING') ";
            };

            sql2 += "ORDER BY CT DESC LIMIT 10";

            OdbcConnection con2 = new OdbcConnection(connectionString);
            OdbcCommand cmd2 = new OdbcCommand(sql2, con2);
            con2.Open();
            OdbcDataReader reader2 = cmd2.ExecuteReader();
            Chart2.DataSource = reader2;
            Chart2.DataBind();

            Chart2.Series["Series1"].ToolTip = "#VALX\nCount: #VALY";
            
            reader2.Close();
            con2.Close();


            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            string sql3 = "SELECT Neighborhood, ZipCode, AvgIncome, BelowPovertyLine, Population ";
            sql3 += "FROM Demographics WHERE (Neighborhood = '" + QueryLocation1 + "') ";
            sql3 += "ORDER BY ZipCode";

            OdbcConnection con3 = new OdbcConnection(connectionString);
            OdbcCommand cmd3 = new OdbcCommand(sql3, con3);
            con3.Open();
            OdbcDataReader reader3 = cmd3.ExecuteReader();
            GridView2.DataSource = reader3;
            GridView2.DataBind();
            reader3.Close();
            con3.Close();


            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            string sql4 = "SELECT Neighborhood, ZipCode, AvgIncome, BelowPovertyLine, Population ";
            sql4 += "FROM Demographics WHERE (Neighborhood = '" + QueryLocation2 + "') ";
            sql4 += "ORDER BY ZipCode";

            OdbcConnection con4 = new OdbcConnection(connectionString);
            OdbcCommand cmd4 = new OdbcCommand(sql4, con4);
            con4.Open();
            OdbcDataReader reader4 = cmd4.ExecuteReader();
            GridView1.DataSource = reader4;
            GridView1.DataBind();
            reader4.Close();
            con4.Close();

            Label1.Text = QueryLocation1 ;
            Label2.Text = QueryLocation2 ;
        }
        finally
        {
            //con1.Close();
        }
    }
    
    protected void ListBox1_SelectedIndexChanged(object sender, EventArgs e)
    {
    }

    protected void ListBox2_SelectedIndexChanged(object sender, EventArgs e)
    {
    }

    protected void GridView1_SelectedIndexChanged(object sender, EventArgs e)
    {
    }

    protected void GridView2_SelectedIndexChanged(object sender, EventArgs e)
    {
    }
    protected void Chart1_Click(object sender, ImageMapEventArgs e)
    {

    }
}
