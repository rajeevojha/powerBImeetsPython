# "Changed Type with Locale" = Table.TransformColumnTypes(#"Previous Step", {{"Ship Date", type date, "en-US"}})
# Day2: Some data transformations
**Learned**: remove duplicate, split and merge, replace
**Challanges**: data manipulation specially in case of date formatting can be challenging
**Method**: First messed the sample data and then cleaned it up
**MQuery**: 
let
    Source = Csv.Document(File.Contents("C:\Users\Rajeev\devl\powerBImeetsPython\datasets\train-messy.csv"),[Delimiter=",", Columns=18, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Row ID", Int64.Type}, {"Order ID", type text}, {"Order Date", type text}, {"Ship Date", type text}, {"Ship Mode", type text}, {"Customer ID", type text}, {"Customer Name", type text}, {"Segment", type text}, {"Country", type text}, {"City", type text}, {"State", type text}, {"Postal Code", Int64.Type}, {"Region", type text}, {"Product ID", type text}, {"Category", type text}, {"Sub-Category", type text}, {"Product Name", type text}, {"Sales", type number}}),
    #"Replaced Value" = Table.ReplaceValue(#"Changed Type","/"," ",Replacer.ReplaceText,{"Order Date"}),
    #"Split Column by Delimiter" = Table.SplitColumn(#"Replaced Value", "Order Date", Splitter.SplitTextByDelimiter(" ", QuoteStyle.Csv), {"Order Date.1", "Order Date.2", "Order Date.3"}),
    #"Changed Type1" = Table.TransformColumnTypes(#"Split Column by Delimiter",{{"Order Date.1", Int64.Type}, {"Order Date.2", type text}, {"Order Date.3", Int64.Type}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type1",{"Row ID", "Order ID", "Order Date.2", "Order Date.1", "Order Date.3", "Ship Date", "Ship Mode", "Customer ID", "Customer Name", "Segment", "Country", "City", "State", "Postal Code", "Region", "Product ID", "Category", "Sub-Category", "Product Name", "Sales"}),
    #"Merged Columns" = Table.CombineColumns(Table.TransformColumnTypes(#"Reordered Columns", {{"Order Date.1", type text}, {"Order Date.3", type text}}, "en-US"),{"Order Date.2", "Order Date.1", "Order Date.3"},Combiner.CombineTextByDelimiter("/", QuoteStyle.None),"Order Date"),
    #"Changed Type2" = Table.TransformColumnTypes(#"Merged Columns",{{"Order Date", type date}})
in
    #"Changed Type2"
**Challenges**: Hit a ‘DataFormat.Error’ on Ship Date ("July 14 2016"). Fixed by using ‘Change Type with Locale’ to parse it as a date; still a long way to go